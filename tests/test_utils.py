import unittest
from app.utils.api_client import APIClient

class APIClientTestCase(unittest.TestCase):
    def test_get(self):
        response = APIClient.get('services')
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()
