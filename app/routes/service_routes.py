from flask import Blueprint, jsonify
from app.services.service_service import ServiceService

service_bp = Blueprint('service', __name__)

@service_bp.route('/services', methods=['GET'])
def get_services():
    services = ServiceService.get_all_services()
    return jsonify(services)

@service_bp.route('/services/<int:service_id>/incidents', methods=['GET'])
def get_incidents_by_service(service_id):
    incidents = ServiceService.get_incidents_by_service(service_id)
    return jsonify(incidents)

@service_bp.route('/services/<int:service_id>/incidents/by_status', methods=['GET'])
def get_incidents_by_service_and_status(service_id):
    incidents_by_status = ServiceService.get_incidents_by_service_and_status(service_id)
    return jsonify(incidents_by_status)