import json
import boto3
import logging
import uuid
from boto3.dynamodb.conditions import Key
from decimal import Decimal

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
conferences_table = dynamodb.Table('conferences')
ratings_table = dynamodb.Table('ratings')

def decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    # Log the incoming event
    logger.info("Received event: %s", json.dumps(event))
    
    # Extract HTTP method and path from the event
    http_method = event['requestContext']['http']['method']
    path = event['rawPath']
    
    if http_method == 'GET' and path == '/conferences':
        response = conferences_table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'], default=decimal_to_float)
        }
    
    elif http_method == 'POST' and path == '/feedback':
        # Parse the request body
        body = json.loads(event['body'])
        conference_id = body.get('conferenceId')
        rating = body.get('rating')
        comment = body.get('comment')
        
        # Generate a unique rating ID
        rating_id = str(uuid.uuid4())
        
        # Insert the feedback into the ratings table
        ratings_table.put_item(
            Item={
                'conferenceId': conference_id,
                'ratingId': rating_id,
                'rating': Decimal(str(rating)),
                'comment': comment
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Feedback submitted successfully')
        }
    
    elif http_method == 'GET' and path.startswith('/conferences/') and path.endswith('/rating'):
        # Extract conference ID from the path
        conference_id = path.split('/')[2]
        
        # Query the ratings table for the given conference ID
        response = ratings_table.query(
            KeyConditionExpression=Key('conferenceId').eq(conference_id)
        )
        
        # Calculate the overall rating
        ratings = [item['rating'] for item in response['Items']]
        overall_rating = float(sum(ratings) / len(ratings)) if ratings else 0.0
        
        return {
            'statusCode': 200,
            'body': json.dumps(overall_rating)
        }
    
    elif http_method == 'GET' and path.startswith('/conferences/') and path.endswith('/comments'):
        # Extract conference ID from the path
        conference_id = path.split('/')[2]
        
        # Query the ratings table for the given conference ID
        response = ratings_table.query(
            KeyConditionExpression=Key('conferenceId').eq(conference_id)
        )
        
        # Extract comments and ratings
        comments_with_ratings = [
            {'rating': float(item['rating']), 'comment': item['comment']}
            for item in response['Items']
        ]
        
        return {
            'statusCode': 200,
            'body': json.dumps(comments_with_ratings, default=decimal_to_float)
        }
    
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported method or path')
        } 