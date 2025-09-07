
from flask import Blueprint, request, jsonify
from app.models import Task, Employee
from app import db
from .project_routes import get_project_name

employee_bp = Blueprint('employee_bp', __name__)


# ✅ Get All Projects
@employee_bp.route('/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    result = []
    for employee in employees:
        created_date= employee.created_date.strftime("%d-%m-%Y") if (employee.created_date is not None) else None
        last_name = employee.last_name if (employee.last_name is not None) else ''
        project_name = get_project_name(employee.project_id)
        result.append({
            'id': employee.id,
            'first_name': employee.first_name,
            'last_name': last_name,
            'is_active': employee.is_active,
            'project_id': employee.project_id,
            'task_id': employee.task_id,
            'created_date': created_date,
            'project_name': project_name,
        })

    return jsonify(result), 200

# ✅ Create Task
@employee_bp.route('/create', methods=['POST'])
def create_employee():
    data = request.get_json()
    if not data or 'first_name' not in data:
        return jsonify({'error': 'first_name is required'}), 400

    new_employee = Employee(
        first_name=data['first_name'],
        last_name=data.get('last_name', ''),
        is_active=data.get('is_active', False),
        project_id=data.get('project_id',None),
        task_id=data.get('task_id',None),
        created_date=data.get('created_date',None)
    )

    db.session.add(new_employee)
    db.session.commit()

    return jsonify({
        'id': new_employee.id,
        'first_name': new_employee.first_name,
        'last_name': new_employee.last_name,
        'is_active': new_employee.is_active,
        'project_id': new_employee.project_id,
        'task_id':new_employee.task_id,
        'created_date':new_employee.created_date
    }), 201