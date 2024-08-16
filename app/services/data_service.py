from app import db
from app.models.service import Service
from app.models.incident import Incident
from app.models.team import Team
from app.models.escalation_policy import EscalationPolicy
from app.utils.api_client import APIClient

class DataService:
    @staticmethod
    def save_services():
        services = APIClient.get_services()['services']
        for service in services:
            team_id = service['team']['id'] if 'team' in service and 'id' in service['team'] else None
            db_service = Service(id=service['id'], name=service['name'], team_id=team_id)
            db.session.add(db_service)
        db.session.commit()

    @staticmethod
    def save_incidents():
        incidents = APIClient.get_incidents()['incidents']
        for incident in incidents:
            db_incident = Incident(id=incident['id'], status=incident['status'], service_id=incident['service']['id'])
            db.session.add(db_incident)
        db.session.commit()

    @staticmethod
    def save_teams():
        teams = APIClient.get_teams()['teams']
        for team in teams:
            db_team = Team(id=team['id'], name=team['name'])
            db.session.add(db_team)
        db.session.commit()

    @staticmethod
    def save_escalation_policies():
        policies = APIClient.get_escalation_policies()['escalation_policies']
        for policy in policies:
            team_id = policy['team']['id'] if 'team' in policy and 'id' in policy['team'] else None
            db_policy = EscalationPolicy(id=policy['id'], name=policy['name'], team_id=team_id)
            db.session.add(db_policy)
        db.session.commit()