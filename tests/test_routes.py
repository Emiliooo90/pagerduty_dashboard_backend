import unittest
import asyncio
from app.utils.api_client import APIClient
from unittest.mock import patch, AsyncMock

class APIClientTestCase(unittest.IsolatedAsyncioTestCase):
    @patch('app.utils.api_client.aiohttp.ClientSession.get', new_callable=AsyncMock)
    async def test_get(self, mock_get):
        # Test the get method of the APIClient class
        # Implement the test logic here
        mock_response = {'services': [{'id': '1', 'name': 'Service1'}]}
        mock_get.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
        
        services = await APIClient.get_services()
        self.assertEqual(services, mock_response)

if __name__ == '__main__':
    unittest.main()