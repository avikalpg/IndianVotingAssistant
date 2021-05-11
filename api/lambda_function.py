import json

def lambda_handler(event, context):
    loc = event
    if 'lat' in loc.keys() and 'long' in loc.keys():
        if isinstance(loc['lat'], float) and isinstance(loc['long'], float):
            resObj = dict()
            resObj['latitude'] = loc['lat']
            resObj['longitude'] = loc['long']
            return {
                'statusCode': 200,
                'body': json.dumps(resObj)
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps("'lat' and 'long' must be floating point numbers. Received: (" + str(loc['lat']) + ", " + str(loc['long']))
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps("request body must contain fields 'lat' and 'long'")
        }
