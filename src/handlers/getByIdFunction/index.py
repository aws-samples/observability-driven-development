import os
import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
tableName = os.environ['SAMPLE_TABLE']
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    try:
        print (event)
        # Parse input from the event
        key = event['pathParameters']['id']
        print (key)
        # Retrieve the item from DynamoDB
        response = table.get_item(
            Key={
                'id': key  
            }
        )
        
        # Check if the item was found
        if 'Item' in response:
            item = response['Item']
            print (item)
            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            return {
                'statusCode': 404,
                'body': 'Item not found'
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }        