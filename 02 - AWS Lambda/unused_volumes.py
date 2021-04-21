import boto3


client = boto3.client('ec2')
volumes = client.describe_volumes()
unused_volumes = []
size = 0
for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 0:
        unused_volumes.append(volume['VolumeId'])
        size += volume['Size']
        print(volume)
        print("-----" * 5)


email_body = "####### Unused Volumes ####### \n"
email_body += "Total Unused Volumes Size: {} \n\n".fomat(size)
for volumeId in unused_volumes:
    email_body += "VolumeId: {} \n".format(volumeId)

sns_arn = ''
sns_client = boto3.client('sns')
sns_client.publish (
    TopicArn=sns_arn,
    Subject = 'Unused Volumes',
    Message = email_body
)
