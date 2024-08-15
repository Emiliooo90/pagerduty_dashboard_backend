from flask import Blueprint, jsonify
from app.services.team_service import TeamService

team_bp = Blueprint('team', __name__)

@team_bp.route('/teams', methods=['GET'])
def get_teams():
    teams = TeamService.get_all_teams()
    return jsonify(teams)
