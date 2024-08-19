import unittest
from unittest.mock import patch, AsyncMock
from app.utils.api_client import APIClient

class APIClientTestCase(unittest.IsolatedAsyncioTestCase):
    @patch('app.utils.api_client.aiohttp.ClientSession.get')
    async def test_get(self, mock_get):
        # Create a mock response
        mock_response = AsyncMock()
        mock_response.json.return_value = {'services': [{'id': '1', 'name': 'Service1'}]}
        
        # Make the mock_get return an async context manager
        mock_context_manager = AsyncMock()
        mock_context_manager.__aenter__.return_value = mock_response
        mock_get.return_value = mock_context_manager

        result = await APIClient.get_services()
        
        # Assert your expectations here
        self.assertIsInstance(result, dict)
        self.assertIn('services', result)
        self.assertIsInstance(result['services'], list)
        self.assertEqual(len(result['services']), 1)
        self.assertEqual(result['services'][0]['id'], '1')
        self.assertEqual(result['services'][0]['name'], 'Service1')

        # Verify the mock was called correctly
        mock_get.assert_called_once_with(
            f"{APIClient.BASE_URL}/services",
            headers=APIClient.HEADERS,
            params={'limit': 100}
        )

if __name__ == '__main__':
    unittest.main()