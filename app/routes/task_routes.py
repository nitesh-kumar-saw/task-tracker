# Task-related endpoints
from flask import Blueprint, request, jsonify
from app.models import Task
from app import db

task_bp = Blueprint('task_bp', __name__)

# ✅ Create Task
@task_bp.route('', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'Pending')
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        'id': new_task.id,
        'title': new_task.title,
        'description': new_task.description,
        'status': new_task.status,
        'created_at': new_task.created_at
    }), 201


# ✅ Get All Tasks
@task_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    result = []

    for task in tasks:
        result.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'created_at': task.created_at
        })

    return jsonify(result), 200
