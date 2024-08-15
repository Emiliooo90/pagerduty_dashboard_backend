import unittest
from app import create_app, db
from app.models.service import Service

class ServiceRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_services(self):
        service = Service(name='Test Service')
        db.session.add(service)
        db.session.commit()

        with self.app.test_client() as client:
            response = client.get('/services')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 1)
            self.assertEqual(response.json()[0]['name'], 'Test Service')

if __name__ == '__main__':
    unittest.main()
