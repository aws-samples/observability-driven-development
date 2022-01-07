import os
import boto3
from boto3.dynamodb.conditions import Key, Attr
import datetime

DOCS = """
## Returns average price per ride and total revenue
```"""

dynamodb = boto3.resource('dynamodb')
# tableName = boto3.client('dynamodb').list_tables()['TableNames'][0]
tableName = os.environ['DYNAMODB_TABLE_NAME']
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    response = table.scan(FilterExpression=Attr('timestamp').between(int(datetime.datetime.now().timestamp()*1000)-60*15*1000,int(datetime.datetime.now().timestamp()*1000)))
    data = response['Items']
    totalprice = 0
    count = 1
    for item in data:
        totalprice += int(item["price"])
        count += 1
    if count == 0:
        average = 0
    else:
        average = round(totalprice/count, 2)

    return "<h1> Number of rides: " + str(count) + "</h1><br><h1> total revenue: " + str(totalprice) + "</h1><br><h1> average revenue per ride: " + str(average) + "</h1>"