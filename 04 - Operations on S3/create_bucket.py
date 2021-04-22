import boto3
client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='joacbatista1994',
    CreateBucketConfiguration={
        'LocationConstraint': 'sa-east-1'
    }
)
