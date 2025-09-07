from app import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default='Defined')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.Date,default=datetime.utcnow)
    priority = db.Column(db.String(10),nullable=False)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    owner = db.Column(db.String, nullable=True)
    is_project_done = db.Column(db.Boolean, default=False)     
    created_by = db.Column(db.String(100), default='System')
    start_date = db.Column(db.Date,nullable=True)
    end_date = db.Column(db.Date,nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=True)
    is_active = db.Column(db.Boolean, default=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)