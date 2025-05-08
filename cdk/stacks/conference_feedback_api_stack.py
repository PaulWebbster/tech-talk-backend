from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_lambda as lambda_
)
from constructs import Construct
import json

class ConferenceFeedbackApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda Layer
        lambda_layer = _lambda.LayerVersion(
            self, "FeedbackApiLayer",
            code=_lambda.Code.from_asset("../lambda_layer"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="A layer for feedback API dependencies"
        )

        # Define the Lambda function
        lambda_function = _lambda.Function(
            self, "FeedbackApiLambda",
            function_name="FeedbackApiLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("../src"),
            layers=[lambda_layer],
            environment={
                "AWS_ACCOUNT_ID": "585994675900"
            }
        )

        # Load the policy from the JSON file
        with open('dynamodb_policy.json') as f:
            policy_document = json.load(f)

        # Create a policy from the document
        policy = iam.Policy(self, "DynamoDBPolicy",
            document=iam.PolicyDocument.from_json(policy_document)
        )

        # Attach the policy to the Lambda function
        lambda_function.role.attach_inline_policy(policy)

        # Create a function URL for the Lambda function
        function_url = lambda_.FunctionUrl(
            self, "FunctionUrl",
            function=lambda_function,
            auth_type=lambda_.FunctionUrlAuthType.NONE  # Set to NONE for public access
        )

        # Output the function URL
        self.url_output = function_url.url