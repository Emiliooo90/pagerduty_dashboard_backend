from app.models.service import Service
from app import db

class ServiceService:
    @staticmethod
    def get_all_services():
        services = Service.query.all()
        return [service.to_dict() for service in services]

    @staticmethod
    def to_dict(service):
        return {
            'id': service.id,
            'name': service.name,
            'team_id': service.team_id
        }