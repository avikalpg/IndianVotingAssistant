from src import app
from flask import jsonify, request

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
	
	# TODO: Implement the function
	return jsonify({'error':'Function not implemented'})

@app.route('/getConstituencyFromVoterId', methods=['GET','POST'])
def getConstituencyFromVoterId():
	voter_id = request.json.get('voter_id') if request.method == 'POST' else request.args.get('voter_id')
	if not voter_id:
		return jsonify({'error':"request body must contain the field 'voter_id'"}), 400
	elif not isinstance(lat, str):
		return jsonify({'error':"field 'voter_id' must be of type str"}), 400
	
	# TODO: Implement the function
	return jsonify({'error':'Function not implemented'})

@app.route('/getConstituencyFromVoterIdCardImage', methods=['POST'])
def getConstituencyFromVoterIdCardImage():	
	# TODO: Implement the function
	return jsonify({'error':'Function not implemented'})