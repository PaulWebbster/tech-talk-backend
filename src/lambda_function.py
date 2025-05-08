import json
import boto3
import logging
from boto3.dynamodb.conditions import Key

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('conferences')

def lambda_handler(event, context):
    # Log the incoming event
    logger.info("Received event: %s", json.dumps(event))
    
    # Extract HTTP method and path from the event
    http_method = event['requestContext']['http']['method']
    path = event['rawPath']
    
    if http_method == 'GET' and path == '/conferences':
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