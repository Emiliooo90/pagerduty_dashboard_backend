# PagerDuty Dashboard Backend

This is the PagerDuty Dashboard Backend created with Python for the Customer Success Group Innovation Team Take Home Exercise.

## Project Overview

This backend application interacts with the PagerDuty API to extract data, store it in a MySQL database, and provide endpoints for dashboard analysis. It focuses on analyzing services, incidents, teams, and escalation policies.

## Features

- Fetch and store data from PagerDuty API
- Provide RESTful endpoints for dashboard data
- Generate CSV reports
- Perform data analysis and visualization

## Tech Stack

- Python 3.10
- Flask
- SQLAlchemy
- MySQL
- Docker
- Pandas
- Pytest
- Asyncio

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/Emiliooo90/pagerduty_dashboard_backend.git
   cd pagerduty_dashboard_backend
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Docker Support

To run the application using Docker Compose:

1. Build and start the containers:
   ```
   docker-compose build
   docker-compose up
   ```

2. Run database migrations:
   ```
   docker-compose exec web flask db init
   docker-compose exec web flask db migrate -m "Initial migration"
   docker-compose exec web flask db upgrade
   ```

3. The API will be available at `http://127.0.0.1:5001/`

To stop the application:
```
docker-compose down -v
```

## API Endpoints
- GET `/services`: Get the list of services
- GET `/services/<int:service_id>/incidents`: Get the list of incidents for a specific service
- GET `/services/<int:service_id>/incidents/by_status`: Get the list of incidents for a specific service filtered by status
- GET `/services/count`: Get the count of services
- GET `/services/incidents/count`: Get the count of incidents per service
- GET `/services/incidents/by_status/count`: Get the count of incidents per service filtered by status
- GET `/services/incidents/analyze`: Analyze incidents
- GET `/incidents`: Get the list of incidents
- GET `/incidents/analysis`: Analyze incidents
- GET `/view_incident_graph`: View incident graph
- GET `/teams`: Get the list of teams
- GET `/teams/services/count`: Get the count of teams and services
- GET `/escalation-policies`: Get the list of escalation policies
- GET `/escalation_policies/csv`: Get the list of escalation policies in CSV format
- GET `/fetch_and_save`: Fetch and save data from PagerDuty API

## Testing

Run unit and integration tests:

```
pytest
```