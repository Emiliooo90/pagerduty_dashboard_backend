from flask import Blueprint, jsonify
from app.services.team_service import TeamService
from app.services.service_service import ServiceService
from app.services.escalation_policy_service import EscalationPolicyService
from app import db

team_bp = Blueprint('team', __name__)

@team_bp.route('/teams', methods=['GET'])
def get_teams():
    teams = TeamService.get_all_teams()
    return jsonify(teams)

@team_bp.route('/teams/services/count', methods=['GET'])
def count_teams_and_services():
    service_service = ServiceService(db.session)
    teams_services_count = service_service.count_teams_and_services()
    return jsonify(teams_services_count)

@team_bp.route('/teams/escalation_policies/count', methods=['GET'])
def count_escalation_policies_and_relationships():
    escalation_policy_service = EscalationPolicyService(db.session)
    policies_count = escalation_policy_service.count_policies_and_relationships()
    return jsonify(policies_count)