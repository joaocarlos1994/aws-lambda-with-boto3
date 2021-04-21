import boto3
import json


s3_client = boto3.client('s3')
dynamodb_resource = boto3.resource('dynamodb')


def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    file_object = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    fileReader = file_object['Body'].read()
    jsonDict = json.loads(fileReader)

    dynamodb_table = dynamodb_resource.Table('emploees')
    dynamodb_table.put_item(Item=jsonDict)
