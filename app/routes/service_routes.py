from flask import Blueprint, jsonify
from app.services.service_service import ServiceService
from app import db

service_bp = Blueprint('service', __name__)

@service_bp.route('/services', methods=['GET'])
def get_services():
    service_service = ServiceService(db.session)
    services = service_service.get_all_services()
    return jsonify(services)

@service_bp.route('/services/count', methods=['GET'])
def count_services():
    service_service = ServiceService(db.session)
    count = service_service.count_services()
    return jsonify({'service_count': count})

@service_bp.route('/services/incidents/count', methods=['GET'])
def count_incidents_per_service():
    service_service = ServiceService(db.session)
    incidents_count = service_service.count_incidents_per_service()
    return jsonify(incidents_count)


@service_bp.route('/services/incidents/by_status/count', methods=['GET'])
def count_incidents_by_service_and_status():
    service_service = ServiceService(db.session)
    incidents_by_status = service_service.count_incidents_by_service_and_status()
    
    # Ensure all values are integers
    total_count = sum(
        sum(int(value) for value in status_counts.values() if isinstance(value, (int, str)) and str(value).isdigit())
        for status_counts in incidents_by_status if isinstance(status_counts, dict)
    )
    
    response = {
        'incidents_by_status': incidents_by_status,
        'total_count': total_count
    }
    return jsonify(response)


@service_bp.route('/services/incidents/analyze', methods=['GET'])
def analyze_incidents():
    service_service = ServiceService(db.session)
    analysis = service_service.analyze_incidents()
    return jsonify(analysis)