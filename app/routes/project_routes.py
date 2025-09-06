from flask import Blueprint, request, jsonify
from app.models import Project
from app import db

project_bp = Blueprint('project_bp', __name__)

# ✅ Create Task
@project_bp.route('/create', methods=['POST'])
def create_project():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Project name is required'}), 400
    
    new_project = Project(
        name=data.get('name'),
        description=data.get('description', ''),
        owner=data.get('owner', ''),
        is_project_done=data.get('is_project_done'),
        start_date=data.get('start_date'),
        end_date=data.get('end_date')
    )

    db.session.add(new_project)
    db.session.commit()

    return jsonify({
        'id': new_project.id,
        'name': new_project.name,
        'description': new_project.description,
        'owner': new_project.owner,        
        'is_project_done':new_project.is_project_done,
        'created_by':new_project.created_by,
        'start_date':new_project.start_date,
        'end_date':new_project.end_date,
        'created_date': new_project.created_date        
    }), 201

# ✅ Get All Projects
@project_bp.route('/', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    result = []

    for project in projects:
        start_date = project.start_date.strftime("%d-%m-%Y") if (project.start_date is not None) else None
        end_date = project.end_date.strftime("%d-%m-%Y") if (project.end_date is not None) else None
        created_date = project.created_date.strftime("%d-%m-%Y") if (project.created_date is not None) else None

        result.append({
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'owner': project.owner,        
            'is_project_done':project.is_project_done,
            'created_by':project.created_by,
            'start_date':start_date,
            'end_date': end_date,
            'created_date': created_date
        })

    return jsonify(result), 200

# ✅ Get All Projects
@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get(project_id)

    if not project:
        return jsonify({'error': 'Project not found'}), 404

    return jsonify({
        'id': project.id,
        'name': project.name,
        'description': project.description,
        'owner': project.owner,
        'is_project_done':project.is_project_done,
        'created_by':project.created_by,
        'start_date':project.start_date.strftime("%Y-%m-%d") if (project.start_date is not None) else None,
        'end_date': project.end_date.strftime("%Y-%m-%d") if (project.end_date is not None) else None,
        'created_date': project.created_date.strftime("%Y-%m-%d") if (project.created_date is not None) else None
    }), 200


@project_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get(project_id)
    data = request.json
    if not project or 'name' not in data:
        return jsonify({'error': 'Project not found'}), 400

    project.name = data.get("name", project.name)
    project.description = data.get("description", project.description)
    project.start_date = data.get("start_date", project.start_date)
    project.end_date = data.get("end_date", project.end_date)
    project.owner = data.get("owner", project.owner)
    project.is_project_done = data.get("is_project_done", project.is_project_done)
    db.session.commit()

    return jsonify({"message": "Project updated successfully", "project": {'id': project.id, 'name': project.name, 'description': project.description, 'owner': project.owner,
                    'is_project_done': project.is_project_done, 'created_by': project.created_by,
                    'start_date': project.start_date, 'end_date': project.end_date,
                    'created_date': project.created_date}}), 201