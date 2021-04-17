import boto3

client = boto3.client("ec2")

response = client.describe_instances(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running', 'terminated']
        },
    ])

for reservations in response['Reservations']:
    for instances in reservations['Instances']:
        print(instances['InstanceId'])
