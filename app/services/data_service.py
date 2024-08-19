from app import db
from app.models.service import Service
from app.models.incident import Incident
from app.models.team import Team
from app.models.escalation_policy import EscalationPolicy
from app.utils.api_client import APIClient
import logging
import asyncio
import pandas as pd

class DataService:
    
    @staticmethod
    def save_services():
        try:
            # Fetch services and teams
            services = asyncio.run(APIClient.get_services())['services']
            teams = asyncio.run(APIClient.get_teams())['teams']
            
            # Create a DataFrame for services
            services_df = pd.DataFrame(services)
            logging.info(f"Number of services fetched: {len(services_df)}")
            
            # Create a dictionary for teams
            team_dict = {team['id']: team for team in teams}
            
            for _, service in services_df.iterrows():
                logging.info(f"Processing service: {service}")
                try:
                    # Get the team data for the service
                    team_id = service.get('team', {}).get('id')
                    team = team_dict.get(team_id)
                    
                    db_service = Service(
                        id=service['id'],
                        name=service['name'],
                        description=service.get('description'),  # New field
                        status=service.get('status'),  # New field
                        created_at=service.get('created_at'),  # New field
                        updated_at=service.get('updated_at'),  # New field
                        team_id=team_id,
                    )
                    db.session.add(db_service)
                    logging.info(f"Service added to session: {service['id']}")
                except Exception as e:
                    logging.error(f"Error adding service {service['id']} to session: {e}")
            try:
                db.session.commit()
                logging.info("Services saved successfully")
            except Exception as e:
                logging.error(f"Error committing services to database: {e}")
                db.session.rollback()
        except Exception as e:
            logging.error(f"Error fetching services: {e}")
            db.session.rollback()

    @staticmethod
    def save_incidents():
        try:
            mock_data = {
                "incidents": [
                    {
                        "id": "PT4KHLK",
                        "status": "resolved",
                        "service": {
                            "id": "PIJ90N7"
                        }
                    },
                    {
                        "id": "PT4KHL2",
                        "status": "unresolved",
                        "service": {
                            "id": "PIJ90N8"
                        }
                    },
                    {
                        "id": "PT4KHL3",
                        "status": "acknowledged",
                        "service": {
                            "id": "PIJ90N9"
                        }
                    }
                ],
                "limit": 3,
                "offset": 0,
                "more": False
            }

            incidents = [
                Incident(
                    id=incident['id'],
                    status=incident['status'],
                    service_id=incident['service']['id']
                )
                for incident in mock_data['incidents']
            ]

            db.session.bulk_save_objects(incidents)
            db.session.commit()
            logging.info("Incidents saved successfully")
        except Exception as e:
            logging.error(f"Error saving incidents: {e}")
            db.session.rollback()

    @staticmethod
    def save_teams():
        try:
            teams = asyncio.run(APIClient.get_teams())['teams']
            teams_df = pd.DataFrame(teams)
            logging.info(f"Number of teams fetched: {len(teams_df)}")
            
            for _, team in teams_df.iterrows():
                db_team = Team(id=team['id'], name=team['name'])
                db.session.add(db_team)
            db.session.commit()
            logging.info("Teams saved successfully")
        except Exception as e:
            logging.error(f"Error saving teams: {e}")
            db.session.rollback()

    @staticmethod
    def save_escalation_policies():
        try:
            policies = asyncio.run(APIClient.get_escalation_policies())['escalation_policies']
            policies_df = pd.DataFrame(policies)
            logging.info(f"Number of escalation policies fetched: {len(policies_df)}")
            
            for _, policy in policies_df.iterrows():
                team_id = policy['team']['id'] if 'team' in policy and 'id' in policy['team'] else None
                db_policy = EscalationPolicy(id=policy['id'], name=policy['name'], team_id=team_id)
                db.session.add(db_policy)
            db.session.commit()
            logging.info("Escalation policies saved successfully")
        except Exception as e:
            logging.error(f"Error saving escalation policies: {e}")
            db.session.rollback()

    @staticmethod
    def insert_services():
        services = [
            Service(id='1', name='Service1', team_id='1'),
            Service(id='2', name='Service2', team_id='2'),
            # Add more services as needed
        ]
        db.session.bulk_save_objects(services)
        db.session.commit()

    @staticmethod
    def insert_incidents():
        incidents = [
            Incident(id='1', status='resolved', service_id='P2MC68J'),
            Incident(id='2', status='unresolved', service_id='P3R0EI5'),
            # Add more incidents as needed
        ]
        db.session.bulk_save_objects(incidents)
        db.session.commit()

    @staticmethod
    def insert_teams():
        teams = [
            Team(id='1', name='Team1'),
            Team(id='2', name='Team2'),
            # Add more teams as needed
        ]
        db.session.bulk_save_objects(teams)
        db.session.commit()

    @staticmethod
    def insert_escalation_policies():
        policies = [
            EscalationPolicy(id='1', name='Policy1', team_id='1'),
            EscalationPolicy(id='2', name='Policy2', team_id='2'),
            # Add more policies as needed
        ]
        db.session.bulk_save_objects(policies)
        db.session.commit()