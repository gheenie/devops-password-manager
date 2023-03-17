import pytest
import os
from moto import mock_secretsmanager
import boto3
from moto.core import patch_client
from src.password_manager import (secrets_manager, create_secret, list_secrets)


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""

    os.environ['AWS_ACCESS_KEY_ID'] = 'test'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
    os.environ['AWS_SECURITY_TOKEN'] = 'test'
    os.environ['AWS_SESSION_TOKEN'] = 'test'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'


@pytest.fixture(scope='function')
def premock_secretsmanager(aws_credentials):
    with mock_secretsmanager():
        # yield boto3.client('secretsmanager', region_name='us-east-1')
        yield 'unused string, this is just to prevent mock from closing'


def test_valid_secrets_successfully_stores_in_secretsmanager(premock_secretsmanager):
    # patch_client(secrets_manager)

    output = create_secret()
    
    assert output == 'Secret saved.'


def test_creating_existing_secret_throws_error(premock_secretsmanager):
    # patch_client(secrets_manager)

    create_secret()
    output = create_secret()

    assert output == 'Secret ID already exists.'


def test_list_secrets__no_secrets(premock_secretsmanager):
    output = list_secrets()

    assert output == '0 secret(s) available'


def test_list_secrets__secrets_do_exist(premock_secretsmanager):
    create_secret()
    create_secret(secret_id='secret_id2', user_id='user2', password='password2')
    output = list_secrets()

    assert output == '2 secret(s) available\nMissile_Launch_Codes2\nsecret_id2'
