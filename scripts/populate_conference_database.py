import boto3

def main():
    # Initialize a session using your AWS credentials
    session = boto3.Session(
        profile_name='cloud-native',
        region_name='eu-west-1'
    )

    # Initialize DynamoDB resource
    dynamodb = session.resource('dynamodb')

    # Reference the table
    table = dynamodb.Table('conferences')

    # List of conferences to add
    conferences = [
        {"conferenceId": "1", "date": "2024-04-15", "name": "AWS Summit London", "keywords": "AWS, Cloud, Serverless"},
        {"conferenceId": "2", "date": "2024-05-20", "name": "Google Cloud Next", "keywords": "GCP, Cloud, AI/ML"},
        {"conferenceId": "3", "date": "2024-06-10", "name": "Microsoft Build", "keywords": "Azure, Cloud, AI"},
        {"conferenceId": "4", "date": "2024-07-15", "name": "KubeCon Europe", "keywords": "Kubernetes, Cloud Native, DevOps"},
        {"conferenceId": "5", "date": "2024-08-20", "name": "AWS re:Invent", "keywords": "AWS, Cloud, Innovation"},
        {"conferenceId": "6", "date": "2024-09-10", "name": "Google Cloud Summit", "keywords": "GCP, Cloud, Data"},
        {"conferenceId": "7", "date": "2024-10-15", "name": "Microsoft Ignite", "keywords": "Azure, Cloud, Security"},
        {"conferenceId": "8", "date": "2024-11-20", "name": "AWS Summit Berlin", "keywords": "AWS, Cloud, Architecture"},
        {"conferenceId": "9", "date": "2024-12-10", "name": "Google Cloud Next Europe", "keywords": "GCP, Cloud, Analytics"},
        {"conferenceId": "10", "date": "2025-01-15", "name": "Microsoft Build Europe", "keywords": "Azure, Cloud, Development"}
    ]

    # Add conferences to the table
    for conference in conferences:
        table.put_item(Item=conference)

    print("Conferences added successfully.")

if __name__ == "__main__":
    main()
