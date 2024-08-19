import unittest
from app.utils.api_client import APIClient

class APIClientTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_get(self):
        response = await APIClient.get('services')
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()
