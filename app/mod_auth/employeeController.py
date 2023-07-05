from flask import request, render_template, redirect, url_for, Blueprint, jsonify
import app.mod_employee.service as employee_service
from app.mod_employee.models import Employee
from app import app
from app import db
from datetime import datetime

app03 = Blueprint('employee', __name__)


# 增加一条工作人员信息
@app.route('/addEmployee', methods=['POST'])
def addEmployee():
    response = {}
    if request.form.get('profile_photo'):
        profile_photo = request.form.get('profile_photo')
    else:
        profile_photo = '/'
    employee = Employee(
        username=request.form.get('username'),
        gender=request.form.get('gender'),
        phone=request.form.get('phone'),
        id_card=request.form.get('id_card'),
        birthday=request.form.get('birthday'),
        hire_date=request.form.get('hire_date'),
        description=request.form.get('description'),
        profile_photo=profile_photo,
        isactive='yes',
        created=datetime.now()
    )
    db.session.add(employee)
    db.session.commit()
    response['code'] = 200
    response['message'] = 'Successfully added employee'
    return response


# 修改工作人员信息
@app.route('/updateEmployee/<int:id>', methods=['POST'])
def updateEmployee(id):
    response = {}
    targetEmployee = employee_service.select_by_id(id)
    if targetEmployee:
        if request.form.get('username'):
            targetEmployee.username = request.form.get('username')
        if request.form.get('gender'):
            targetEmployee.gender = request.form.get('gender')
        if request.form.get('phone'):
            targetEmployee.phone = request.form.get('phone')
        if request.form.get('id_card'):
            targetEmployee.id_card = request.form.get('id_card')
        if request.form.get('birthday'):
            targetEmployee.birthday = request.form.get('birthday')
        if request.form.get('hire_date'):
            targetEmployee.hire_date = request.form.get('hire_date')
        if request.form.get('description'):
            targetEmployee.description = request.form.get('description')
        if request.form.get('resign_date'):
            targetEmployee.resignDate = request.form.get('resign_date')
        if request.form.get('isactive'):
            targetEmployee.isactive = request.form.get('isactive')
        if request.form.get('imgset_dir'):
            targetEmployee.imgset_dir = request.form.get('imgset_dir')
        if request.form.get('profile_photo'):
            targetEmployee.profile_photo = request.form.get('profile_photo')
        targetEmployee.updated = datetime.now()

        db.session.commit()  # 提交更新到数据库
        response['code'] = 200
        response['message'] = 'Employee updated successfully'
    else:
        response['code'] = 404
        response['message'] = 'Employee not found'
    return response


# 根据id删除工作人员信息
@app.route('/deleteEmployee/<int:id>', methods=['POST'])
def deleteEmployee(id):
    response = {}
    targetEmployee = employee_service.select_by_id(id)
    if targetEmployee:
        db.session.delete(targetEmployee)
        db.session.commit()  # 提交更新到数据库
        response['code'] = 200
        response['message'] = 'Employee deleted successfully'
    else:
        response['code'] = 404
        response['message'] = 'Employee not found'
    return response


# 查询所有工作人员信息
@app.route('/getAllEmployee')
def getAllEmployee():
    response = {}
    employees = employee_service.get_all_employee()
    response['code'] = 200
    employee_json = []
    for employee in employees:
        employee_data = employee.to_dict()
        employee_json.append(employee_data)
    response['data'] = employee_json
    return response


# 根据姓名模糊查询工作人员信息
@app.route('/getEmployee/<string:name>')
def getEmployee(name):
    response = {}
    employees = Employee.query.filter(Employee.username.contains(name)).all()
    response['code'] = 200
    employee_json = []
    for employee in employees:
        employee_data = employee.to_dict()
        employee_json.append(employee_data)
    response['data'] = employee_json
    return response


# 更新工作人员头像
@app.route('/updateEmployeeImage/<int:id>', methods=['POST'])
def updateEmployeeImage(id):
    response = {}
    targetEmployee = employee_service.select_by_id(id)
    if targetEmployee:
        if request.form.get('profile_photo'):
            targetEmployee.profile_photo = request.form.get('profile_photo')
        targetEmployee.updated = datetime.now()

        db.session.commit()  # 提交更新到数据库
        response['code'] = 200
        response['message'] = 'Successfully modified the employee profile'
    else:
        response['code'] = 404
        response['message'] = 'Employee not found'
    return response