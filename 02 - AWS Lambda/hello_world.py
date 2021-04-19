import json

def lambda_handler(event, context):
    reponse = 'Hi {}, welcome to the lambda functions'.format(event['name'])
    return {
        'statusCode': 200,
        'body': json.dumps(reponse)
    }
