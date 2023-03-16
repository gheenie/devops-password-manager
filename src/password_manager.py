import boto3
import json


secrets_manager = boto3.client('secretsmanager')


def create_secret():
    secret_id = 'Missile_Launch_Codes2'
    user_id = 'bidenj'
    password = 'pa55word'
    secret_json = { 'user_id': user_id, 'password': password }

    try:
        secrets_manager.create_secret(
            Name=secret_id,
            SecretString=json.dumps(secret_json)
        )

        return 'Secret saved.'
    except Exception as e:
        print(e)
        
        return 'An unexpected error occured.'

# response = create_secret()
# print(response)


def list_secrets():
    pass
