from src import app
from flask import jsonify, request

@app.route('/getCandidatesFromElection', methods['GET', 'POST'])
def getCandidatesFromElection():
    # TODO: Implement the function
	return jsonify({'error':'Function not implemented'})

@app.route('/getCandidateDetails/<string:candidate_id>')
def getCandidateDetails():
    # TODO: Implement the function
	return jsonify({'error':'Function not implemented'})