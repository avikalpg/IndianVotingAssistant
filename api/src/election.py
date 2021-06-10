from src import app
from flask import jsonify, request
import requests
import pandas as pd

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
	r = requests.get('https://eci.gov.in/elections/future-elections/')
	print(r.status_code)
	if r.status_code == 200:
		table_val = __getTableInformationFromHTML(r.text)
		return jsonify(table_val)
	else:
		return jsonify({'error':'Could not reach Election Commission of India\'s website'})

def __getTableInformationFromHTML(html_text: str):
	all_data = []
	tables = pd.read_html(html_text)
	for table in tables:
		data = table.to_dict(orient='records')
		if len(data) > 0:
			all_data.append(data)
	return all_data