import unittest
import lambda_function as lf
import json

class TestLambdaFunction(unittest.TestCase):
    def test_field_name_check(self):
        req = dict()

        # both, lat and long missing
        req['message'] = "This is unnecessary text"
        res = lf.lambda_handler(req, None)
        self.assertEqual(res['statusCode'], 400)

        # long missing
        req['lat'] = 19.001
        res = lf.lambda_handler(req, None)
        self.assertEqual(res['statusCode'], 400)

        # both present
        req['long'] = 73.149
        res = lf.lambda_handler(req, None)
        self.assertEqual(res['statusCode'], 200)

        # lat missing
        req.pop('lat')
        res = lf.lambda_handler(req, None)
        self.assertEqual(res['statusCode'], 400)

    def test_field_value_type_check(self):
        req = dict()
        req['lat'] = 'a'
        req['long'] = 73.0
        res = lf.lambda_handler(req, None)
        self.assertEqual(res['statusCode'], 400)

        req['lat'] = 32.121
        req['long'] = 2
        res = lf.lambda_handler(req, None)
        self.assertEqual(res['statusCode'], 400)

        req['long'] = 2.12
        res = lf.lambda_handler(req, None)
        self.assertEqual(res['statusCode'], 200)

if __name__ == '__main__':
    unittest.main()
