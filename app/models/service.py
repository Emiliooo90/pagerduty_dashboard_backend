from app import db
from app.models.team import Team  # Import the Team model

class Service(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=True)  # New field
    status = db.Column(db.String(64), nullable=True)  # New field
    created_at = db.Column(db.String(64), nullable=True)  # New field
    updated_at = db.Column(db.String(64), nullable=True)  # New field
    team_id = db.Column(db.String(30), db.ForeignKey('team.id'), nullable=True)
    team = db.relationship('Team', backref='services', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,  # New field
            'status': self.status,  # New field
            'created_at': self.created_at,  # New field
            'updated_at': self.updated_at,  # New field
            'team_id': self.team_id
        }

    @staticmethod
    def save_service_with_team(service_data, team_data):
        # Find or create the team
        team = Team.query.filter_by(id=team_data['id']).first()
        if not team:
            team = Team(id=team_data['id'], name=team_data.get('name'))
            db.session.add(team)
            db.session.commit()

        # Create the service
        service = Service(
            id=service_data['id'],
            name=service_data['name'],
            description=service_data.get('description'),
            status=service_data.get('status'),
            created_at=service_data.get('created_at'),
            updated_at=service_data.get('updated_at'),
            team_id=team.id
        )
        db.session.add(service)
        db.session.commit()
        return service