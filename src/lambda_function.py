import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('conferences')

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET' and event['path'] == '/conferences':
        response = table.scan()
        return {
            'statusCode': 200,
            'body': response['Items']
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported method or path')
        } 