from app.models.escalation_policy import EscalationPolicy
from app import db
from sqlalchemy import func
from app.models.team import Team
from app.models.service import Service

class EscalationPolicyService:
    def __init__(self, db_session):
        self.db_session = db_session

    @staticmethod
    def get_all_policies():
        policies = EscalationPolicy.query.all()
        return [policy.to_dict() for policy in policies]

    @staticmethod
    def to_dict(policy):
        return {
            'id': policy.id,
            'name': policy.name,
            'team_id': policy.team_id
        }

    def count_policies_and_relationships(self):
        policies = self.db_session.query(
            EscalationPolicy.id,
            EscalationPolicy.name,
            Team.name.label('team_name'),
            func.count(Service.id).label('service_count')
        ).outerjoin(Team, EscalationPolicy.team_id == Team.id
        ).outerjoin(Service, Team.id == Service.team_id
        ).group_by(EscalationPolicy.id, Team.name).all()

        return [{'policy_id': policy.id, 'policy_name': policy.name, 'team_name': policy.team_name, 'service_count': policy.service_count} for policy in policies]