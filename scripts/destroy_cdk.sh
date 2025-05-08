#!/bin/bash

# Navigate to the cdk directory
cd cdk

# Activate the virtual environment
source .venv/bin/activate

# Destroy the CDK stack
cdk destroy --force

# Deactivate the virtual environment
deactivate

echo "CDK stack destroyed successfully." 