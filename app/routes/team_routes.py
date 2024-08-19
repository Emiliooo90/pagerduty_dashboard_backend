from flask import Blueprint, jsonify
from app.services.team_service import TeamService
from app.services.service_service import ServiceService

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