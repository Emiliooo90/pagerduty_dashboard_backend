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
            services = asyncio.run(APIClient.get_services())['services']
            services_df = pd.DataFrame(services)
            logging.info(f"Number of services fetched: {len(services_df)}")
            
            for _, service in services_df.iterrows():
                db_service = Service(
                    id=service['id'],
                    name=service['name']
                )
                db.session.add(db_service)
            db.session.commit()
            logging.info("Services saved successfully")
        except Exception as e:
            logging.error(f"Error saving services: {e}")
            db.session.rollback()

    @staticmethod
    def save_incidents():
        try:
            incidents = asyncio.run(APIClient.get_incidents())['incidents']
            incidents_df = pd.DataFrame(incidents)
            logging.info(f"Number of incidents fetched: {len(incidents_df)}")
            
            for _, incident in incidents_df.iterrows():
                db_incident = Incident(
                    id=incident['id'],
                    status=incident['status'],
                    service_id=incident['service']['id']
                )
                db.session.add(db_incident)
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