from flask import Blueprint, jsonify
from app.services.incident_service import IncidentService

incident_bp = Blueprint('incident', __name__)

@incident_bp.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = IncidentService.get_all_incidents()
    return jsonify(incidents)
