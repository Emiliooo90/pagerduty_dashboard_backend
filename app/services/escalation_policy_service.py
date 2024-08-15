from app.models.escalation_policy import EscalationPolicy
from app import db

class EscalationPolicyService:
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
