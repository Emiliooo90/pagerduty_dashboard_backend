from app import db

class Team(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }