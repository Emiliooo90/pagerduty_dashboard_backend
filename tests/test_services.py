import pytest
import asyncio
from app import create_app, db
from app.models.service import Service

@pytest.fixture
async def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:emilio12345678.@localhost:3306/pagerdutydatabase'
    async with app.test_client() as client:
        async with app.app_context():
            db.create_all()
            yield client
        db.drop_all()

@pytest.mark.asyncio
async def test_get_services(client):
    service = Service(id='1', name='Service1')
    db.session.add(service)
    db.session.commit()
    
    response = await client.get('/services')
    assert response.status_code == 200
    assert response.json == [{'id': '1', 'name': 'Service1', 'team_id': None}]