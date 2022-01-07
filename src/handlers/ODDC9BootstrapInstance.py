from __future__ import print_function
import boto3
import json
import os
import time
import traceback
import cfnresponse
import jsonpickle

def lambda_handler(event, context):
    # logger.info('event: {}'.format(event))
    # logger.info('context: {}'.format(context))
    responseData = {}

    if event['RequestType'] == 'Create':
        try:
            # Open AWS clients
            ec2 = boto3.client('ec2')

            # Get the InstanceId of the Cloud9 IDE
            instance = ec2.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['aws-cloud9-'+event['ResourceProperties']['StackName']+'-'+event['ResourceProperties']['EnvironmentId']]}])['Reservations'][0]['Instances'][0]
            # logger.info('instance: {}'.format(instance))

            # Create the IamInstanceProfile request object
            iam_instance_profile = {
                'Arn': event['ResourceProperties']['LabIdeInstanceProfileArn'],
                'Name': event['ResourceProperties']['LabIdeInstanceProfileName']
            }
            # logger.info('iam_instance_profile: {}'.format(iam_instance_profile))

            # Wait for Instance to become ready before adding Role
            instance_state = instance['State']['Name']
            # logger.info('instance_state: {}'.format(instance_state))
            while instance_state != 'running':
                time.sleep(5)
                instance_state = ec2.describe_instances(InstanceIds=[instance['InstanceId']])
                # logger.info('instance_state: {}'.format(instance_state))

            # attach instance profile
            response = ec2.associate_iam_instance_profile(IamInstanceProfile=iam_instance_profile, InstanceId=instance['InstanceId'])
            # logger.info('response - associate_iam_instance_profile: {}'.format(response))
            r_ec2 = boto3.resource('ec2')

            responseData = {'Success': 'Started bootstrapping for instance: '+instance['InstanceId']}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, 'CustomResourcePhysicalID')
            
        except Exception as e:
            # logger.error(e, exc_info=True)
            json_data = jsonpickle.encode(e)
            responseData = {'Error:{}'.format(json_data)}
            cfnresponse.send(event, context, cfnresponse.FAILED, responseData, 'CustomResourcePhysicalID')
            
    else:
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, 'CustomResourcePhysicalID')