import boto3
import json
from botocore.exceptions import ClientError


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
    except ClientError as error:
        print(error)

        if error.response['Error']['Code'] == 'ResourceExistsException':
            return 'Secret ID already exists.'
        else:
            return 'An unexpected error occured.'
    except Exception as error:
        print(error)
        
        return 'An unexpected error occured.'


def list_secrets():
    try:
        secret_list = secrets_manager.list_secrets()['SecretList']

        message = f'{len(secret_list)} secret(s) available'

        return message
    except Exception as error:
        print(error)
        
        return 'An unexpected error occured.'


# response = list_secrets()
# print(response)
# response = create_secret()
# print(response)
# response = list_secrets()
# print(response)
