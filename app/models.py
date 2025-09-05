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
