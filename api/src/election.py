from src import app
from flask import jsonify, request

@app.route('/getElectionsFromConstituency', methods=['GET', 'POST'])
def getElectionsFromConstituency():
    # TODO: Implement the function
	return jsonify({'error':'Function not implemented'})

@app.route('/getElectionsFromPartNo', methods=['GET', 'POST'])
def getElectionsFromPartNo():
    # TODO: Implement the function
	return jsonify({'error':'Function not implemented'})

@app.route('/getAllFutureElections', methods=['GET'])
def getAllFutureElections():
    # TODO: Implement the function
    return jsonify({'error':'Function not implemented'})