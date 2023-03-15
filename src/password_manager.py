import boto3
import json


client = boto3.client('secretsmanager')


def create_secret():
    secret_id = 'Missile_Launch_Codes2'
    user_id = 'bidenj'
    password = 'pa55word'
    secret_json = { 'user_id': user_id, 'password': password }

    try:
        response = client.create_secret(
            Name=secret_id,
            SecretString=json.dumps(secret_json)
        )

        return response
    except Exception as e:
        print(e)
        
        return 'An unexpected error occured.'

# response = create_secret()
# print(response)
