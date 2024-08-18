import aiohttp
import asyncio
import logging

class APIClient:
    BASE_URL = 'https://api.pagerduty.com'
    HEADERS = {
        'Authorization': 'Token token=u+b4CCjDZsXfuxx-w_fw',
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Content-Type': 'application/json'
    }

    @staticmethod
    async def get(endpoint):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{APIClient.BASE_URL}/{endpoint}", headers=APIClient.HEADERS) as response:
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