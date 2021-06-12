from datetime import date
import traceback
from typing import Tuple

from werkzeug.exceptions import FailedDependency, Gone
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

@app.route('/getElectionsFromState', methods=['GET', 'POST'])
def getElectionsFromState():
	state_elections, exp = __getNextElectionForState(request.args.get('state', '', type=str))
	if exp != None:
		app.logger.error(''.join(traceback.format_exception(type(exp), exp, exp.__traceback__)))
		return jsonify({'exception':exp.description}), exp.code
	return jsonify(state_elections)

@app.route('/getAllFutureElections', methods=['GET'])
def getAllFutureElections():
	r = requests.get('https://eci.gov.in/elections/future-elections/')
	print("getAllFutureElections", r.status_code)
	if r.status_code == 200:
		table_val = __getTableInformationFromHTML(r.text)
		data = [table.to_dict(orient='records') for table in table_val]
		return jsonify(data)
	else:
		return jsonify({'error':'Could not reach Election Commission of India\'s website'})

def __getTableInformationFromHTML(html_text: str):
	all_data = []
	tables = pd.read_html(html_text)
	for table in tables:
		if len(table) > 0:
			all_data.append(table)
	return all_data

def __getNextElectionForState(stateName: str) -> Tuple[object, Exception]:
	try:
		r = requests.get('https://eci.gov.in/elections/term-of-houses/')
		print("__getNextElectionForState", r.status_code)
		if r.status_code != 200:
			raise Gone("Failed to get Term-of-houses from ECI website", r.raw)
	except Exception as e:
		return None, e

	next_elections = []
	terms_of_houses = __getTableInformationFromHTML(r.text)
	union_elections_terms = terms_of_houses[0]
	state_elections_terms = terms_of_houses[1]

	# extract the date for next lok sabha elections
	try:
		lok_sabha_elections = union_elections_terms[(union_elections_terms['OFFICE/STATE'] == "LOK SABHA") & (union_elections_terms['TO'].str.contains('^\d+\.\d+\.\d+$'))]
		if lok_sabha_elections.shape[0] != 1:
			# there should be only one end-date for lok sabha elections
				raise FailedDependency("Found "+ str(lok_sabha_elections.shape[0]) +" end-dates for the term of lok sabha on ECI website")
	except Exception as e:
		return None, e
	next_elections.append(lok_sabha_elections.to_dict(orient='records')[0])

	# extract the date for next state elections
	try:
		state_elections = state_elections_terms[(state_elections_terms['HOUSE/STATE'] == stateName.upper()) & (state_elections_terms['TO'].str.contains('^\d+\.\d+\.\d+$'))]
		if state_elections.shape[0] != 1:
			# there should be only one end-date for any state's elections
				raise FailedDependency("Found "+ str(state_elections.shape[0]) +" end-dates for the term of " + stateName.upper() + " State on ECI website")
	except Exception as e:
		return None, e
	next_elections.append(state_elections.to_dict(orient='records')[0])

	next_elections.sort(key=lambda df: __getDateFromDateString(df['TO']))

	return next_elections, None

def __getDateFromDateString(date_string: str) -> date:
	day, month, year = [int(k) for k in date_string.split('.')]
	return date(year, month, day)