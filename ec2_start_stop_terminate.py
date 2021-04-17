import boto3

client = boto3.client("ec2")
#response = client.start_instances(InstanceIds=['i-092a9ba8bdc6ed651'])
#for startingInstances in response['StartingInstances']:
#    print(startingInstances['CurrentState'])
#    print(startingInstances['PreviousState'])

#response = client.stop_instances(InstanceIds=['i-092a9ba8bdc6ed651'])
#for startingInstances in response['StoppingInstances']:
#    print(startingInstances['CurrentState'])
#    print(startingInstances['PreviousState'])

response = client.terminate_instances(InstanceIds=['i-092a9ba8bdc6ed651'])
for startingInstances in response['TerminatingInstances']:
    print(startingInstances['CurrentState'])
    print(startingInstances['PreviousState'])
