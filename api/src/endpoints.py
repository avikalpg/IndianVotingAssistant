from flask import jsonify, make_response, request
from src import app, constituency, users

@app.route('/')
def landing():
	return jsonify({'message':'Welcome to Indian Voting Assistant'})

@app.errorhandler(404)
def resource_not_found(e):
	return make_response(jsonify(error='Not found!'), 404)