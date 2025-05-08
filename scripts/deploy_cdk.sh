#!/bin/bash

# Activate the virtual environment
source cdk/.venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }
echo "Activated virtual environment"

# Navigate to the cdk directory
cd cdk

# Deploy the CDK stack
echo "Deploying CDK stack"
cdk deploy

# Deactivate the virtual environment
deactivate

echo "CDK stack deployed successfully." 