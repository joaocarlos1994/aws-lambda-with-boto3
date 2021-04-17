import boto3


client = boto3.client("ec2")


response = client.run_instances(ImageId='ami-0c27c96aaa148ba6d',
                                InstanceType='t2.micro',
                                MinCount=1,
                                MaxCount=1)

for instance in response['Instances']:
    print(instance['InstanceId'])
