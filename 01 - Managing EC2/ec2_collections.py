import boto3

#ec2Resource = boto3.resource("ec2")
#for instance in ec2Resource.instances.all():
#    print('Instance id is {} and instance type is {} '.format(instance.instance_id, instance.instance_type))

ec2Resource = boto3.resource("ec2")
ec2Resource.instances.filter(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]).stop()
