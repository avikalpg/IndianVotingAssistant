import requests
import json
import pytest

@pytest.fixture
def getConstituencyFromLocationUrl(get_base_url):
	url = get_base_url + "getConstituencyFromLocation"
	headers = {
		'Content-Type': 'application/json'
	}
	return url, headers

@pytest.mark.parametrize("req", [
	{"message":"This is unnecessary text"}, # both, lat and long missing
	{'latitude': 19.001}, # long missing
	{'longitude': 73.149}]) # lat missing
def test_api_field_name_check(getConstituencyFromLocationUrl, req):
	url, headers = getConstituencyFromLocationUrl
	res = requests.request("POST", url, headers=headers, data=json.dumps(req))
	assert res.status_code == 400

@pytest.mark.parametrize("lat, lon", [('a', 73.0), (32.121, 2)])
def test_api_field_value_type_check(getConstituencyFromLocationUrl, lat, lon):
	url, headers = getConstituencyFromLocationUrl
	payload = json.dumps({
		"latitude": lat,
		"longitude": lon
	})
	response = requests.request("POST", url, headers=headers, data=payload)
	assert response.status_code == 400

@pytest.mark.parametrize("lat, lon", [(23.12, 83.12), (19.033400, 73.018997)])
def test_api_sanity(getConstituencyFromLocationUrl, lat, lon):
	url, headers = getConstituencyFromLocationUrl
	payload = json.dumps({
		"latitude": lat,
		"longitude": lon
	})
	response = requests.request("POST", url, headers=headers, data=payload)
	assert response.status_code == 200
