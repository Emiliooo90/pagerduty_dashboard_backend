from flask import Blueprint, jsonify
from app.services.escalation_policy_service import EscalationPolicyService

escalation_policy_bp = Blueprint('escalation_policy', __name__)

@escalation_policy_bp.route('/escalation_policies', methods=['GET'])
def get_escalation_policies():
    policies = EscalationPolicyService.get_all_policies()
    return jsonify(policies)
