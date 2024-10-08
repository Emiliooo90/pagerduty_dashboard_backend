from app import db

class EscalationPolicy(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    team_id = db.Column(db.String(30), db.ForeignKey('team.id'), nullable=True)
    team = db.relationship('Team', backref='escalation_policies', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'team_id': self.team_id
        }
