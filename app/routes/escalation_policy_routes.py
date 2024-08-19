from flask import Blueprint, jsonify, Response
import csv
from io import StringIO
from app.services.escalation_policy_service import EscalationPolicyService
from app.services.incident_service import IncidentService  # Assuming this service exists

escalation_policy_bp = Blueprint('escalation_policy', __name__)

@escalation_policy_bp.route('/escalation_policies', methods=['GET'])
def get_escalation_policies():
    policies = EscalationPolicyService.get_all_policies()
    num_policies = len(policies)
    
    for policy in policies:
        policy['num_teams'] = len(policy.get('teams', []))
        policy['num_services'] = len(policy.get('services', []))
    
    response = {
        'num_policies': num_policies,
        'policies': policies
    }
    
    return jsonify(response)

@escalation_policy_bp.route('/escalation_policies/csv', methods=['GET'])
def get_escalation_policies_csv():
    policies = EscalationPolicyService.get_all_policies()
    
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Policy ID', 'Policy Name', 'Number of Teams', 'Number of Services'])
    
    for policy in policies:
        cw.writerow([policy['id'], policy['name'], len(policy.get('teams', [])), len(policy.get('services', []))])
    
    output = si.getvalue()
    return Response(output, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=escalation_policies.csv"})