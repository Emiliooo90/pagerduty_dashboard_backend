from app import db

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(64), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)