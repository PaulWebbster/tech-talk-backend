from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class ConferenceFeedbackApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function
        lambda_function = _lambda.Function(
            self, "ConferenceFeedbackFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("../src"),
            environment={
                "AWS_ACCOUNT_ID": "585994675900"
            }
        ) 