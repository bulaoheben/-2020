import math
from flask import request, Blueprint
from app import db
from app.mod_oldperson.models import OldPersonInfo
import datetime

oldperson = Blueprint('oldperson', __name__)


# 添加老人信息
@oldperson.route('/addOldPerson', methods=['POST'])
def add_old_person():
    response = {}
    username = request.form.get('username')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    id_card = request.form.get('id_card')
    birthday = request.form.get('birthday')

    # 检查数据是否为空
    if not username or not gender or not phone or not id_card or not birthday:
        response['code'] = "23"
        response['message'] = 'Missing required data.'
        return response

    # 检查id_card是否重复
    existing_person = OldPersonInfo.query.filter_by(id_card=id_card).first()
    if existing_person:
        response['code'] = "24"
        response['message'] = 'Old person with the same ID card already exists.'
        return response

    # 创建新的老人信息
    new_person = OldPersonInfo(
        username=username,
        gender=gender,
        phone=phone,
        id_card=id_card,
        birthday=birthday,
        checkin_date=datetime.datetime.now()
    )

    # 将新的老人信息添加到数据库
    db.session.add(new_person)
    db.session.commit()

    # 返回成功消息
    response['code'] = "200"
    response['message'] = 'Old person information added successfully.'
    return response


# 删除老人信息
@oldperson.route('/deleteOldPerson', methods=['DELETE'])
def delete_old_person():
    response = {}

    # 获取请求中的数据
    print(request)
    id_card = request.form.get('id_card')

    # 检查数据是否为空
    if not id_card:
        response['code'] = "23"
        response['message'] = 'Missing required data.'
        return response

    # 检查老人信息是否存在
    person = OldPersonInfo.query.filter_by(id_card=id_card).first()
    if not person:
        response['code'] = "24"
        response['message'] = 'Old person information not found.'
        return response

    # 删除老人信息
    db.session.delete(person)
    db.session.commit()

    # 返回成功消息
    response['code'] = "200"
    response['message'] = 'Old person information deleted successfully.'
    return response


# 修改老人信息
@oldperson.route('/updateOldPerson/<int:person_id>', methods=['PUT'])
def update_old_person(person_id):
    response = {}

    # 检查老人信息是否存在
    person = OldPersonInfo.query.get(person_id)
    if not person:
        response['code'] = "23"
        response['message'] = 'Old person information not found.'
        return response

    # 更新老人信息
    for field in OldPersonInfo.__table__.columns:
        field_name = field.name
        if field_name in request.form and request.form[field_name]:
            setattr(person, field_name, request.form[field_name])

    db.session.commit()

    # 返回成功消息
    response['code'] = "200"
    response['message'] = 'Old person information updated successfully.'
    return response


# 查询特定老人信息
@oldperson.route('/getOldPerson/<int:person_id>', methods=['GET'])
def get_old_person(person_id):
    response = {}

    # 检查老人信息是否存在
    person = OldPersonInfo.query.get(person_id)
    if not person:
        response['code'] = "23"
        response['message'] = 'Old person information not found.'
        return response

    # 返回老人信息
    response['code'] = "200"
    response['message'] = 'Old person information found.'
    response['data'] = person.to_dict()
    return response


# 查询所有老人信息（后端分页查询）
@oldperson.route('/getAllOldPersons', methods=['GET'])
def get_all_old_persons():
    response = {}

    # 获取分页参数
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    # 计算跳过的条目数量
    offset = (page - 1) * per_page

    # 查询老人信息
    persons = OldPersonInfo.query.offset(offset).limit(per_page).all()

    # 查询总条目数
    total_items = OldPersonInfo.query.count()

    # 计算总页数
    total_pages = int(math.ceil(total_items / per_page))

    # 构造分页结果
    person_list = [person.to_dict() for person in persons]

    # 返回分页结果
    response['code'] = "200"
    response['message'] = 'Old person information retrieved successfully.'
    response['data'] = {
        'items': person_list,
        'total_pages': total_pages,
        'total_items': total_items
    }
    return response
