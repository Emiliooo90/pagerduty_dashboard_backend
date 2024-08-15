from flask import Blueprint, jsonify
from app.services.data_service import DataService

data_bp = Blueprint('data', __name__)

@data_bp.route('/fetch_and_save', methods=['GET'])
def fetch_and_save():
    DataService.save_services()
    DataService.save_incidents()
    DataService.save_teams()
    DataService.save_escalation_policies()
    return jsonify({"message": "Data fetched and saved successfully"})
