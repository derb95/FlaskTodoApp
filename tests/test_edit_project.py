import unittest
from database_initialization import db
from flask import Flask
from models import Project
from project_routes import routes_bp

class TestEditProject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app.config['TESTING'] = True
        db.init_app(cls.app)
        cls.app.register_blueprint(routes_bp)
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def setUp(self):
        self.client = self.app.test_client()
        with self.app.app_context():
            # Create a project to edit
            p = Project(name='Original Name')
            db.session.add(p)
            db.session.commit()
            self.project_id = p.id

    def tearDown(self):
        with self.app.app_context():
            db.session.query(Project).delete()
            db.session.commit()

    def test_update_project_success(self):
        with self.app.app_context():
            response = self.client.post(f'/update_project/{self.project_id}', data={'project_name': 'Updated Name'})
            self.assertEqual(response.status_code, 302)  # Redirect
            updated_project = Project.query.get(self.project_id)
            self.assertEqual(updated_project.name, 'Updated Name')

    def test_update_project_missing_name(self):
        with self.app.app_context():
            response = self.client.post(f'/update_project/{self.project_id}', data={'project_name': ''})
            # Should probably redirect or handle error. According to common practice, redirect back.
            self.assertEqual(response.status_code, 302)
            project = Project.query.get(self.project_id)
            self.assertEqual(project.name, 'Original Name')

if __name__ == '__main__':
    unittest.main()
