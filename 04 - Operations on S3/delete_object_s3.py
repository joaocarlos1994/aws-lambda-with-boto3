import boto3
client = boto3.client('s3')

response = client.delete_object(
    Bucket='joacbatista1994',
    Key='create_bucket.py'
)
