import os
import json
import boto3
import logging
from datetime import datetime
import base64

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
tableName = os.environ['SAMPLE_TABLE']
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    try:
        if event.get('isBase64Encoded'):
            record = base64.b64decode(event["body"]).decode('utf-8')
        else:
            record = event["body"]

        data = json.loads(record)

        id = data["id"]
        name = data["name"]
        milesTraveled = data["milesTraveled"]
        totalTravelTime = data["totalTravelTime"]
        price = data["price"]
        tenantId = data["tenantId"]
        timestamp = datetime.now().isoformat(timespec='seconds')

        data = { "id": id, "name": name, "timestamp": timestamp, "milesTraveled": milesTraveled, "totalTravelTime": totalTravelTime, "price": price, "tenantId": tenantId }
        # Write the item to DynamoDB
        response = table.put_item(
            Item=data
        )
        print ("Writing to DynamoDB")

        return {
            'statusCode': 200,
            'body': 'Item added successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }