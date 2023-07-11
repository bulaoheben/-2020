import math

from flask import request, Blueprint

from app.mod_volunteer.models import Volunteer
from app import app, db
import datetime

app_volunteer = Blueprint('volunteer', __name__)


def get_all_user():
    return Volunteer.query.all()


# 1录入、2修改、3查询、4删除、5头像的设定和6统计分析
# 除了id不用给其他的都给

# 1.录入(可以啦）
@app.route('/insert_volunteer_info', methods=['POST'])
def insert_volunteer_info():
    # 获取请求中的数据
    name2 = request.form.get('name')
    gender2 = request.form.get('gender')
    phone2 = request.form.get('phone')
    id_card2 = request.form.get('id_card')
    birthday2 = request.form.get('birthday')
    checkin_date2 = request.form.get('checkin_date')
    checkout_date2 = request.form.get('checkout_date')
    imgset_dir2 = request.form.get('imgset_dir')
    profile_photo2 = request.form.get('profile_photo')
    DESCRIPTION2 = request.form.get('DESCRIPTION')
    ISACTIVE2 = request.form.get('ISACTIVE')
    CREATED2 = request.form.get('CREATED')
    CREATEBY2 = request.form.get('CREATEBY')
    UPDATED2 = request.form.get('UPDATED')
    UPDATEBY2 = request.form.get('UPDATEBY')
    REMOVE2 = request.form.get('REMOVE')

    volunteer2 = Volunteer(
        name=name2,
        gender=gender2,
        phone=phone2,
        id_card=id_card2,
        birthday=birthday2,
        checkin_date=checkin_date2,
        checkout_date=checkout_date2,
        imgset_dir=imgset_dir2,
        profile_photo=profile_photo2,
        DESCRIPTION=DESCRIPTION2,
        ISACTIVE=ISACTIVE2,
        CREATED=CREATED2,
        CREATEBY=CREATEBY2,
        UPDATED=UPDATED2,
        UPDATEBY=UPDATEBY2,
        REMOVE=REMOVE2
    )
    db.session.add(volunteer2)
    db.session.commit()

    response = {}
    # 用户名已存在，返回失败消息
    response['code'] = 200
    response['message'] = 'Volunteer information incerted successfully'
    return response


# 2修改义工信息（可以啦）
@app.route('/modify_volunteer_info', methods=['POST'])
def modify_volunteer_info():
    id = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    id_card = request.form.get('id_card')
    birthday = request.form.get('birthday')
    checkin_date = request.form.get('checkin_date')
    checkout_date = request.form.get('checkout_date')
    imgset_dir = request.form.get('imgset_dir')
    profile_photo = request.form.get('profile_photo')
    DESCRIPTION2 = request.form.get('DESCRIPTION')
    ISACTIVE2 = request.form.get('ISACTIVE')
    CREATED2 = request.form.get('CREATED')
    CREATEBY2 = request.form.get('CREATEBY')
    UPDATED2 = request.form.get('UPDATED')
    UPDATEBY2 = request.form.get('UPDATEBY')
    REMOVE2 = request.form.get('REMOVE')

    volunteer = Volunteer.query.get_or_404(id)
    # 更新 volunteer 的属性
    if name:
        volunteer.name = name
    if gender:
        volunteer.gender = gender
    if phone:
        volunteer.phone = phone
    if id_card:
        volunteer.id_card = id_card
    if birthday:
        volunteer.birthday = birthday
    if checkin_date:
        volunteer.checkin_date = checkin_date
    if checkout_date:
        volunteer.checkout_date = checkout_date
    if imgset_dir:
        volunteer.imgset_dir = imgset_dir
    if profile_photo:
        volunteer.profile_photo = profile_photo
    if DESCRIPTION2:
        volunteer.DESCRIPTION = DESCRIPTION2
    if ISACTIVE2:
        volunteer.ISACTIVE2 = ISACTIVE2
    if CREATED2:
        volunteer.CREATED = CREATED2
    if CREATEBY2:
        volunteer.CREATEBY = CREATEBY2
    if UPDATED2:
        volunteer.UPDATED = UPDATED2
    if UPDATEBY2:
        volunteer.UPDATEBY = UPDATEBY2
    if REMOVE2:
        volunteer.REMOVE2 = REMOVE2
    # 提交修改到数据库
    db.session.commit()
    response = {}
    response['code'] = 200
    response['message'] = 'Volunteer information updated successfully'
    return response


# 3.查询义工信息(可以啦）
@app.route('/select_by_id', methods=['POST'])
def select_by_id() -> Volunteer:
    id2 = int(request.form.get('id'))
    volunteer = Volunteer.query.get(id2)
    response = {}
    #    volunteer= Volunteer.query.filter_by(id=id2)
    response['data'] = volunteer.to_dict()
    response['code'] = 200
    return response


# 4.删除义工信息(可以啦)
@app.route('/delete_volunteer_info', methods=['POST'])
def delete_volunteer_info():
    id2 = request.form.get('id')
    volunteer2 = Volunteer.query.get(id2)
    try:
        db.session.delete(volunteer2)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    response = {}
    response['message'] = 'Volunteer information deleted successfully'
    response['code'] = 200
    return response


# 5.头像设定（可以啦）
@app.route('/modify_avator_info', methods=['POST'])
def modify_avator_info():
    id2 = request.form.get('id')
    imgset_dir = request.form.get('imgset_dir')
    volunteer2 = Volunteer.query.get(id2)
    try:
        volunteer2.imgset_dir = imgset_dir
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    response = {}
    response['message'] = 'Volunteer avator modified successfully'
    response['code'] = 200
    return response


# 6.统计分析(入职，离职时间统计）(可以啦)
@app.route('/volunteerrecord', methods=['POST'])
def volunteerrecord():
    column_data = Volunteer.query.with_entities(Volunteer.birthday).all()
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
        elif age <= 10:
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


@app.route('/getAllVolunteers', methods=['GET'])
def getAllVolunteers():
    response = {}

    # 获取分页参数
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    # 计算跳过的条目数量
    offset = (page - 1) * per_page

    # 查询志愿者信息
    persons = Volunteer.query.offset(offset).limit(per_page).all()

    # 查询总条目数
    total_items = Volunteer.query.count()

    # 计算总页数
    total_pages = int(math.ceil(total_items / per_page))

    # 构造分页结果
    person_list = [person.to_dict() for person in persons]

    # 返回分页结果
    response['code'] = "200"
    response['message'] = 'Volunteer information retrieved successfully.'
    response['data'] = {
        'items': person_list,
        'total_pages': total_pages,
        'total_items': total_items
    }
    return response
