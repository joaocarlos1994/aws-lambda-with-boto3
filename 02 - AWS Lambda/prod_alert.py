import boto3

sns_resource = boto3.resource("sns")

def lambda_handler(event, context):
    topic_arn = ""
    message = "Prod server stopped please lookinto it"
    sns_resource.publish(
        TopicArn=topic_arn,
        Message=message
    )
    return pass
