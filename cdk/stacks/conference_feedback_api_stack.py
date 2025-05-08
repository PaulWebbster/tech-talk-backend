from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

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