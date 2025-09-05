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
        status=data.get('status', 'Defined'),
        deadline=data.get('deadline',''),
        priority=data.get('priority','')
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        'id': new_task.id,
        'title': new_task.title,
        'description': new_task.description,
        'status': new_task.status,
        'created_at': new_task.created_at,
        'deadline':new_task.deadline,
        'priority':new_task.priority
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
            'created_at': task.created_at,
            'deadline':task.deadline.strftime("%d-%m-%Y"),
            'priority':task.priority
        })

    return jsonify(result), 200

@task_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority":task.priority,
        "deadline":task.deadline.strftime("%Y-%m-%d")
    })

@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.json
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    task.priority = data.get("priority", task.priority)
    task.deadline = data.get("deadline", task.deadline)

    db.session.commit()
    return jsonify({"message": "Task updated", "task": {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority":task.priority,
        "deadline":task.deadline
    }})


# ✅ Delete Task
@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    print(task)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": f"Task {task_id} deleted"})
