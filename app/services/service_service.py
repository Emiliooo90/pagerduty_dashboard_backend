from app.models.service import Service
from app.models.incident import Incident
from app.models.team import Team
from app import db
import logging
from sqlalchemy import func

class ServiceService:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_services(self):
        services = self.db_session.query(Service).all()
        logging.info(f"Number of services in the database: {len(services)}")
        return [service.to_dict() for service in services]

    def count_services(self):
        return self.db_session.query(Service).count()

    def count_incidents_per_service(self):
        incidents = self.db_session.query(
            Incident.service_id, 
            func.count(Incident.id).label('incident_count')
        ).group_by(Incident.service_id).all()
        
        # Add logging to debug the query results
        logging.info(f"Incidents count per service: {incidents}")
        
        total_count = sum(count for _, count in incidents)
        
        return {
            'total_count': total_count,
            'details': [{'service_id': service_id, 'incident_count': count} for service_id, count in incidents]
        }

    def count_incidents_by_service_and_status(self):
        incidents = self.db_session.query(Incident.service_id, Incident.status, func.count(Incident.id).label('incident_count')).group_by(Incident.service_id, Incident.status).all()
        return [{'service_id': service_id, 'status': status, 'incident_count': count} for service_id, status, count in incidents]

    def count_teams_and_services(self):
        teams = self.db_session.query(Team.id, Team.name, func.count(Service.id).label('service_count')).outerjoin(Service, Team.id == Service.team_id).group_by(Team.id).all()
        return [{'team_id': team_id, 'team_name': name, 'service_count': count} for team_id, name, count in teams]

    def analyze_incidents(self):
        incidents = self.count_incidents_per_service()
        incidents_by_status = self.count_incidents_by_service_and_status()
        most_incidents_service = max(incidents['details'], key=lambda x: x['incident_count'])
        return {
            'most_incidents_service': most_incidents_service,
            'incidents_by_status': incidents_by_status
        }

    @staticmethod
    def to_dict(service):
        return {
            'id': service.id,
            'name': service.name,
            'team_id': service.team_id
        }