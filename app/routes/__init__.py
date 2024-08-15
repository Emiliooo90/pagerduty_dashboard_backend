from flask import Blueprint

def register_routes(app):
    from app.routes.service_routes import service_bp
    from app.routes.incident_routes import incident_bp
    from app.routes.team_routes import team_bp
    from app.routes.escalation_policy_routes import escalation_policy_bp
    from app.routes.data_routes import data_bp

    app.register_blueprint(service_bp)
    app.register_blueprint(incident_bp)
    app.register_blueprint(team_bp)
    app.register_blueprint(escalation_policy_bp)
    app.register_blueprint(data_bp)
