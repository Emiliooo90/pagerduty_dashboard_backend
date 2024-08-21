import aiohttp
import asyncio
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class APIClient:
    BASE_URL = 'https://api.pagerduty.com'
    HEADERS = {
        'Authorization': f"Token token={os.getenv('API_KEY')}",
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Content-Type': 'application/json'
    }

    @staticmethod
    async def get(endpoint, params=None):
        if params is None:
            params = {}
        params['limit'] = 100
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{APIClient.BASE_URL}/{endpoint}", headers=APIClient.HEADERS, params=params) as response:
                response.raise_for_status()
                return await response.json()

    @staticmethod
    async def get_services():
        response = await APIClient.get('services')
        logging.info(f"API response for services: {response}")
        return response

    @staticmethod
    async def get_incidents():
        return await APIClient.get('incidents')

    @staticmethod
    async def get_teams():
        return await APIClient.get('teams')

    @staticmethod
    async def get_escalation_policies():
        return await APIClient.get('escalation_policies')