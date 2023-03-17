import boto3
import json
from botocore.exceptions import ClientError
import os


secrets_manager = boto3.client('secretsmanager')


def create_secret(secret_id = 'Missile_Launch_Codes2', user_id = 'bidenj', password = 'pa55word'):
    try:
        secret_json = { 'user_id': user_id, 'password': password }

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
        for secret in secret_list:
            message += '\n' + secret['Name']

        return message
    except Exception as error:
        print(error)
        
        return 'An unexpected error occured.'


def retrieve_secret(secret_id):
    try:
        output_filename = 'secret.txt'
        output_path = f'data/{output_filename}'
        
        secret_string = secrets_manager.get_secret_value(SecretId=secret_id)['SecretString']

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(secret_string)

        return f'Secrets stored in local file {output_filename}'
    except Exception as error:
        print(error)
        
        return 'An unexpected error occured.'


# response = list_secrets()
# print(response)
# response = create_secret()
# print(response)
# response = list_secrets()
# print(response)
