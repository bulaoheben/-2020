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
            # 离职的工作人员信息无效
            targetEmployee.isactive = 'no'
        if request.form.get('isactive'):  # yse or no
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


# 统计分析(年龄段统计）
@app.route('/getEmployeeRecord', methods=['POST'])
def getEmployeeRecord():
    # 需要只返回在职的工作人员
    column_data = Employee.query.with_entities(Employee.birthday).all()
    # 定义年龄段
    age_ranges = {"00-10": 0, "10-20": 0, "20-30": 0, "30-40": 0,
                  "40-50": 0, "50-60": 0, "60-70": 0, "70-80": 0, "80+": 0}
    for dob in column_data:
        age = datetime.datetime.now().year - dob[0].year
        if age >= 10 and age < 20:
            age_ranges["10-20"] += 1
        elif age >= 20 and age < 30:
            age_ranges["20-30"] += 1
        elif age >= 30 and age < 40:
            age_ranges["30-40"] += 1
        elif age >= 40 and age < 50:
            age_ranges["40-50"] += 1
        elif age >= 50 and age < 60:
            age_ranges["50-60"] += 1
        elif age >= 60 and age < 70:
            age_ranges["60-70"] += 1
        elif age >= 70 and age < 80:
            age_ranges["70-80"] += 1
        elif age <=10:
            age_ranges["00-10"] += 1
        else:
            age_ranges["80+"] += 1

    # 打印每个年龄段的人数
    for range_name, count in age_ranges.items():
        print(f"{range_name}: {count}")

    response = {}
    response['code'] = 200
    data = age_ranges
    response['data'] = data
    return response