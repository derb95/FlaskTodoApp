from flask import request, redirect, url_for, render_template
from models import Task, Project
from database_initialization import db
from routes import routes_bp
from datetime import datetime

@routes_bp.route('/add_task', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        new_task = Task(task=task_content, complete=False)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('routes.home'))


@routes_bp.route('/toggle_task_complete/<int:task_id>')
def toggle_task_complete(task_id):
    task = Task.query.get_or_404(task_id)
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('routes.project_tasks', project_id=task.project_id))


@routes_bp.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('routes.project_tasks', project_id=task.project_id))


@routes_bp.route('/project/<int:project_id>/add_task', methods=['POST'])
def add_project_task(project_id):
    project = Project.query.get_or_404(project_id)
    task_content = request.form.get('task')
    task_description = request.form.get('description')  # Get the description from form data
    due_date_str = request.form.get('due_date')
    due_date = None
    if due_date_str:
        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
        except ValueError:
            due_date = None

    if task_content:
        new_task = Task(
            task=task_content,
            description=task_description,  # Save the description
            due_date=due_date,
            complete=False,
            project_id=project_id
        )
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('routes.project_tasks', project_id=project_id))


@routes_bp.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task_record = Task.query.get_or_404(task_id)
    new_task_content = request.form.get('task')
    new_due_date_str = request.form.get('due_date')
    
    if new_task_content:
        task_record.task = new_task_content
    
    if new_due_date_str:
        try:
            task_record.due_date = datetime.strptime(new_due_date_str, '%Y-%m-%d').date()
        except ValueError:
            pass
    else:
        task_record.due_date = None

    db.session.commit()
    
    return redirect(url_for('routes.project_tasks', project_id=task_record.project_id))


