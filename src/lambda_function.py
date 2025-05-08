import json
from pydantic import BaseModel
from aws_lambda_powertools import Logger
import boto3

logger = Logger()

class InputModel(BaseModel):
    key: str

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))
    
    input_data = InputModel(**event)
    
    client = boto3.client('rds-data')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    } 