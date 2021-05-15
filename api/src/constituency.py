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
	return jsonify({'l': [lat, str(type(lat))], 'h':[lon, isinstance(lon, float)]})