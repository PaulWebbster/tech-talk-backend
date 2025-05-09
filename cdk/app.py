#!/usr/bin/env python3
import os

import aws_cdk as cdk
from cdk.cdk_stack import CdkStack
from stacks.conference_feedback_api_stack import ConferenceFeedbackApiStack
from stacks.conference_database_stack import ConferenceFeedbackDatabaseStack


app = cdk.App()

# Instantiate the ConferenceFeedbackApiStack
ConferenceFeedbackApiStack(app, "ConferenceFeedbackApiStack",
    env=cdk.Environment(account="585994675900", region="eu-west-1")
)

# Instantiate the ServerlessPostgresStack
ConferenceFeedbackDatabaseStack(app, "ConferenceFeedbackDatabaseStack",
    env=cdk.Environment(account="585994675900", region="eu-west-1")
)

app.synth()