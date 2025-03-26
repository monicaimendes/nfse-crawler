import boto3
import os

AWS_REGION = "us-east-2"


def get_dynamodb_resource():
    return boto3.resource(
        "dynamodb",
        region_name=AWS_REGION,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )


def send_sns_message(message):
    sns_client = boto3.client("sns", region_name="us-east-2")
    topic_arn = "arn:aws:sns:us-east-2:414301166999:nfse-notifications"

    sns_client.publish(TopicArn=topic_arn, Message=message, Subject="Notificação de NFSE Nacional")
