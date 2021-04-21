import boto3


s3_client = boto3.client('s3')
dynamodb_resource = boto3.resource('dynamodb')


def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    file_object = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    fileReader = file_object['Body'].read().decode('utf-8')
    emploees = fileReader.split("\n")
    for emploee in emploees:
        dynamodb_table = dynamodb_resource.Table('emploees')
        emploeeData = emploee.split(",")
        dynamodb_table.put_item(Item={
            "id": emploeeData[0],
            "name": emploeeData[1],
            "locations": emploeeData[2]
        })
