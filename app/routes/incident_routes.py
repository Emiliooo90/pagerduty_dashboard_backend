from flask import Blueprint, jsonify, request, send_file
from app.services.incident_service import IncidentService
from app.utils.graph_generator import GraphGenerator
import os

incident_bp = Blueprint('incident', __name__)

@incident_bp.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = IncidentService.get_all_incidents()
    return jsonify(incidents)

@incident_bp.route('/incidents/analysis', methods=['GET'])
def analyze_incidents():
    incidents = IncidentService.get_all_incidents()
    service_incident_count = {}
    incident_status_count = {}
    
    for incident in incidents:
        service_id = incident['service_id']
        status = incident['status']
        
        if service_id not in service_incident_count:
            service_incident_count[service_id] = 0
        service_incident_count[service_id] += 1
        
        if status not in incident_status_count:
            incident_status_count[status] = 0
        incident_status_count[status] += 1
    
    most_incidents_service = max(service_incident_count, key=service_incident_count.get)
    
    response = {
        'service_with_most_incidents': most_incidents_service,
        'incident_status_breakdown': incident_status_count
    }
    
    return jsonify(response)

@incident_bp.route('/view_incident_graph', methods=['GET'])
def view_incident_graph():
    # Fetch real data from the service
    incidents = IncidentService.get_all_incidents()
    
    # Process the data to fit the graph generator's requirements
    data = []
    service_incident_count = {}
    
    for incident in incidents:
        service_id = incident['service_id']
        if service_id not in service_incident_count:
            service_incident_count[service_id] = 0
        service_incident_count[service_id] += 1
    
    for service_id, count in service_incident_count.items():
        data.append({"service": service_id, "incident_count": count})
    
    filename = os.path.join('static', 'incident_graph.png')
    
    # Generate the graph
    GraphGenerator.generate_incident_graph(data, filename)
    
    # Serve the generated graph
    return send_file(filename, mimetype='image/png')