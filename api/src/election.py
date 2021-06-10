from src import app
from flask import jsonify, request
import requests
from bs4 import BeautifulSoup as bs

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
	soup = bs(html_text, "html.parser")
	all_data = []
	tables = soup.find_all('table')
	for table in tables:
		print(table['class'])
		tdata = []
		table_bodies = table.find_all('tbody')

		for table_body in table_bodies:
			data = []
			keys = []
			rows = table_body.find_all('tr')
			for row in rows:
				row_data = dict()
				cols = row.find_all('td')
				if len(cols) == 0:
					cols = row.find_all('th')
					keys = [ele.text.strip() for ele in cols]
					continue
				for i, ele in enumerate(cols):
					row_data[keys[i]] = ele.text.strip()
				data.append(row_data)
			if len(data) > 0:
				tdata.append(data)
		if len(tdata) > 0:
			all_data.append(tdata)
	return all_data