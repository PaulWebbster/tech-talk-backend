from aws_cdk import (
    aws_dynamodb as dynamodb,
    Stack
)
from constructs import Construct

class ConferenceFeedbackDatabaseStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a DynamoDB table for conferences
        conferences_table = dynamodb.Table(
            self, "ConferencesTable",
            table_name="conferences",
            partition_key=dynamodb.Attribute(
                name="conferenceId",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="date",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        # Create a DynamoDB table for ratings
        ratings_table = dynamodb.Table(
            self, "RatingsTable",
            table_name="ratings",
            partition_key=dynamodb.Attribute(
                name="conferenceId",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="ratingId",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )