from src import app, dynamodb_client
from flask import jsonify, make_response, request
import os

USERS_TABLE = os.environ['USERS_TABLE']

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

