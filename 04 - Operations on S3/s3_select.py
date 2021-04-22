import boto3
client = boto3.client('s3')

resp = client.select_object_content(
    Bucket='joacbatista1994',
    Key='files/employees',
    Expression='Select s.name, s.email from S3Object s',
    ExpressionType='SQL',
    InputSerialization= {'CSV': {'FileHeaderInfo': 'Use'}},
    OutputSerialization= {'JSON': {}}
)

for event in resp['Payload']:
    if 'Records' in event:
        print(event['Records']['Payload'].decode())
