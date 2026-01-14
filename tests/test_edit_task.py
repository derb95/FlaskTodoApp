import unittest
from flask import Flask
from database_initialization import db
from models import Project, Task
from task_routes import routes_bp
from project_routes import routes_bp as project_routes_bp

class TestEditTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        cls.app.config['TESTING'] = True
        db.init_app(cls.app)
        cls.app.register_blueprint(routes_bp)
        with cls.app.app_context():
            db.create_all()
        cls.client = cls.app.test_client()

    def setUp(self):
        with self.app.app_context():
            project = Project(name="Test Project")
            db.session.add(project)
            db.session.commit()
            self.project_id = project.id
            
            task = Task(task="Original Task", project_id=self.project_id)
            db.session.add(task)
            db.session.commit()
            self.task_id = task.id

    def tearDown(self):
        with self.app.app_context():
            db.session.query(Task).delete()
            db.session.query(Project).delete()
            db.session.commit()

    def test_update_task_success(self):
        response = self.client.post(f'/update_task/{self.task_id}', data={
            'task': 'Updated Task',
            'due_date': '2026-12-31'
        })
        self.assertEqual(response.status_code, 302)
        
        with self.app.app_context():
            task = Task.query.get(self.task_id)
            self.assertEqual(task.task, 'Updated Task')
            self.assertEqual(task.due_date.strftime('%Y-%m-%d'), '2026-12-31')

    def test_update_task_clear_due_date(self):
        # First set a due date
        with self.app.app_context():
            task = Task.query.get(self.task_id)
            from datetime import date
            task.due_date = date(2026, 12, 31)
            db.session.commit()

        # Now update with empty due date
        response = self.client.post(f'/update_task/{self.task_id}', data={
            'task': 'Updated Task',
            'due_date': ''
        })
        self.assertEqual(response.status_code, 302)
        
        with self.app.app_context():
            task = Task.query.get(self.task_id)
            self.assertIsNone(task.due_date)

    def test_update_task_missing_content(self):
        # If content is missing, it should not update but still redirect
        response = self.client.post(f'/update_task/{self.task_id}', data={'task': ''})
        self.assertEqual(response.status_code, 302)
        
        with self.app.app_context():
            task = Task.query.get(self.task_id)
            self.assertEqual(task.task, 'Original Task')

    def test_update_task_not_found(self):
        response = self.client.post('/update_task/999', data={'task': 'New Name'})
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
