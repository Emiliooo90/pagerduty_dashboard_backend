from app.models.service import Service
from app import db
import logging

class ServiceService:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_services(self):
        services = self.db_session.query(Service).all()
        logging.info(f"Number of services in the database: {len(services)}")
        return [service.to_dict() for service in services]

    def count_services(self):
        return self.db_session.query(Service).count()

    @staticmethod
    def to_dict(service):
        return {
            'id': service.id,
            'name': service.name,
            'team_id': service.team_id
        }