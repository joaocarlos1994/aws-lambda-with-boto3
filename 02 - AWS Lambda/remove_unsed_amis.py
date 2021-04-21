import boto3


ec2_client = boto3.client('ec2')


def lambda_handler(event, context):
    instances = ec2_client.describe_instances()
    used_amis = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            used_amis.append(instance['ImageId'])
    unique_amis = remove_duplicate(used_amis)
    return print(used_amis)


custom_images = ec2_client.describe_images(
    Filters=[
            {
                "Name": "state",
                "Value": [
                    'available'
                ]
            },
        ],
    Owners=['self']
)

custom_amis_list = []
for image in custom_images['Images']:
    custom_amis_list.append(image['ImageId'])

for custom_amis in custom_amis_list:
    if custom_amis not in used_amis:
        client.deregistrer_image(ImageId=image['ImageId'])


def remove_duplicate(amis):
    unique_amis = []
    for ami in amis:
        if ami not in unique_amis:
            unique_amis.append(ami)
    return unique_amis
