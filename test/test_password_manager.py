import pytest
import os
from moto import mock_secretsmanager
import boto3
from moto.core import patch_client
from src.password_manager import (client, create_secret)


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""

    os.environ['AWS_ACCESS_KEY_ID'] = 'test'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
    os.environ['AWS_SECURITY_TOKEN'] = 'test'
    os.environ['AWS_SESSION_TOKEN'] = 'test'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'


@pytest.fixture(scope='function')
def secretsmanager(aws_credentials):
    with mock_secretsmanager():
        yield boto3.client('secretsmanager', region_name='us-east-1')


@pytest.fixture
def precreate_secret(secretsmanager):
    create_secret()


def test_valid_secrets_successfully_stores_in_secretsmanager(secretsmanager):
    patch_client(client)

    response = create_secret()
    
    assert response['ARN'].startswith('arn:aws') == True
