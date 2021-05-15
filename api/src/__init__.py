import boto3, os
from flask import Flask

app = Flask(__name__)

dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')
if os.environ.get('IS_OFFLINE'):
	dynamodb_client = boto3.client('dynamodb', region_name='localhost', endpoint_url='http://localhost:8000')

from src import endpoints