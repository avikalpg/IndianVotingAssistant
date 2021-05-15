import os

import boto3
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')

if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client('dynamodb', region_name='localhost', endpoint_url='http://localhost:8000')


USERS_TABLE = os.environ['USERS_TABLE']

@app.route('/')
def landing():
    return jsonify({'message':'Welcome to Indian Voting Assistant'})

@app.route('/getConstituencyFromLocation', methods=['GET','POST'])
def getConstituencyFromLocation():
    try:
        lat = request.json.get('latitude') if request.method == 'POST' else float(request.args.get('latitude'))
        lon = request.json.get('longitude') if request.method == 'POST' else float(request.args.get('longitude'))
    except ValueError:
        return jsonify({'error':"fields 'latitude' and 'longitude' must be of type float"}), 400
    if not lat or not lon:
        return jsonify({'error':"request body must contain float type fields 'latitude' and 'longitude'"}), 400
    elif not isinstance(lat, float) or not isinstance(lon, float):
        return jsonify({'error':"fields 'latitude' and 'longitude' must be of type float"}), 400
    return jsonify({'l': [lat, str(type(lat))], 'h':[lon, isinstance(lon, float)]})


@app.route('/users/<string:user_id>')
def get_user(user_id):
    result = dynamodb_client.get_item(
        TableName=USERS_TABLE, Key={'userId': {'S': user_id}}
    )
    item = result.get('Item')
    if not item:
        return jsonify({'error': 'Could not find user with provided "userId"'}), 404

    return jsonify(
        {'userId': item.get('userId').get('S'), 'name': item.get('name').get('S')}
    )


@app.route('/users', methods=['POST'])
def create_user():
    user_id = request.json.get('userId')
    name = request.json.get('name')
    if not user_id or not name:
        return jsonify({'error': 'Please provide both "userId" and "name"'}), 400

    dynamodb_client.put_item(
        TableName=USERS_TABLE, Item={'userId': {'S': user_id}, 'name': {'S': name}}
    )

    return jsonify({'userId': user_id, 'name': name})


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
