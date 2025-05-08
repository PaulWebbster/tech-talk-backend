import subprocess
import os

def main():
    # Create the virtual environment and install dependencies
    os.makedirs("lambda_layer/python", exist_ok=True)
    subprocess.run(["python3", "-m", "venv", "lambda_layer/venv"])
    subprocess.run(["lambda_layer/venv/bin/pip", "install", "pydantic", "aws-lambda-powertools", "boto3", "-t", "lambda_layer/python"])
    print("Lambda layer built successfully.")

if __name__ == "__main__":
    main() 