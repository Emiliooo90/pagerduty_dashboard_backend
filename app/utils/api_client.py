import requests

class APIClient:
    BASE_URL = 'https://api.pagerduty.com'
    HEADERS = {
        'Authorization': 'Token token=u+b4CCjDZsXfuxx-w_fw',
        'Accept': 'application/vnd.pagerduty+json;version=2'
    }

    @staticmethod
    def get(endpoint):
        response = requests.get(f"{APIClient.BASE_URL}/{endpoint}", headers=APIClient.HEADERS)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_services():
        return APIClient.get('services')

    @staticmethod
    def get_incidents():
        return APIClient.get('incidents')

    @staticmethod
    def get_teams():
        return APIClient.get('teams')

    @staticmethod
    def get_escalation_policies():
        return APIClient.get('escalation_policies')