from app.models.incident import Incident
from app import db

class IncidentService:
    @staticmethod
    def get_all_incidents():
        incidents = Incident.query.all()
        return [incident.to_dict() for incident in incidents]

    @staticmethod
    def to_dict(incident):
        return {
            'id': incident.id,
            'status': incident.status,
            'service_id': incident.service_id
        }
