from app.models.team import Team
from app import db

class TeamService:
    @staticmethod
    def get_all_teams():
        teams = Team.query.all()
        return [team.to_dict() for team in teams]

    @staticmethod
    def to_dict(team):
        return {
            'id': team.id,
            'name': team.name,
            'services': [service.to_dict() for service in team.services]
        }
