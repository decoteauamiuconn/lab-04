import unittest
from flask import Flask, request
import json
from my_server import app

class MyServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), ' you called \n')

    def test_echo(self):
        response = self.app.post('/echo', data={'text': 'Hello!'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'You said: Hello!')

    def test_trial_division(self):
        response = self.app.get('/trial_division/360')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['factors'], [2, 2, 2, 3, 3, 5])

        

#almost the whole thing autocompleted ? thank you copilot

if __name__ == '__main__':
    unittest.main()

        


