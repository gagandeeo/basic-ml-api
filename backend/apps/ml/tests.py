from django.test import TestCase
from rest_framework.test import APIClient

from .income_happ.linear_regression import LinearRegressionAlgo
# Create your tests here.


class MLTests(TestCase):
    def test_lr_algorithm(self):
        input_data = {
            "income": 4.75568027375266
        }
        my_alg = LinearRegressionAlgo()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])


class APITest(TestCase):
    def test_predict_view(self):
        client = APIClient()
        input_data = {
            "income": 4.75568027375266
        }
        api_url = '/api/predict/'
        response = client.post(api_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual("OK", response.data['status'])
