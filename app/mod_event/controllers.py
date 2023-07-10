import math
from flask import request, Blueprint
from app import db
from app.mod_event.models import EventInfo
from app.mod_oldperson.models import OldPersonInfo

event = Blueprint('event', __name__)


# 添加事件信息
@event.route('/addEvent', methods=['POST'])
def add_event():
    response = {}

    # 获取请求中的数据
    event_type = request.form.get('event_type')
    event_date = request.form.get('event_date')
    event_location = request.form.get('event_location')
    event_desc = request.form.get('event_desc')
    oldperson_id = request.form.get('oldperson_id')

    # 检查数据是否为空
    # 如果该事件是陌生人检测事件或者区域入侵事件则无需考虑老人id是否为空
    if (not event_type or not event_date or not event_location or not event_desc or not oldperson_id) and not (
            (event_type == "2" or event_type == "4") and not oldperson_id):
        response['code'] = "23"
        response['message'] = 'Missing required data.'
        return response

    # 检查事件类型是否正确
    if event_type != "0" and event_type != "1" and event_type != "2" and event_type != "3" and event_type != "4":
        response['code'] = "25"
        response['message'] = 'Incorrect event type.'
        return response

    # 如果是与老人有关的事件，则检查对应老人信息是否存在
    if oldperson_id:
        oldperson = OldPersonInfo.query.get(oldperson_id)
        if not oldperson:
            response['code'] = "24"
            response['message'] = 'Old person information not found.'
            return response

    # 创建新的事件信息
    new_event = EventInfo(
        event_type=event_type,
        event_date=event_date,
        event_location=event_location,
        event_desc=event_desc
    )

    if oldperson_id:
        new_event.oldperson_id = oldperson_id

    # 将新的事件信息添加到数据库
    db.session.add(new_event)
    db.session.commit()

    # 返回成功消息
    response['code'] = "200"
    response['message'] = 'Event information added successfully.'
    return response


# 删除事件信息
@event.route('/deleteEvent/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    response = {}

    # 检查事件信息是否存在
    event = EventInfo.query.get(event_id)
    if not event:
        response['code'] = "23"
        response['message'] = 'Event information not found.'
        return response

    # 删除事件信息
    db.session.delete(event)
    db.session.commit()

    # 返回成功消息
    response['code'] = "200"
    response['message'] = 'Event information deleted successfully.'
    return response


# 修改事件信息
@event.route('/updateEvent/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    response = {}

    # 检查事件信息是否存在
    event = EventInfo.query.get(event_id)
    if not event:
        response['code'] = "23"
        response['message'] = 'Event information not found.'
        return response

    # 如果是与老人有关的事件，则检查对应老人信息是否存在
    oldperson_id = request.form['oldperson_id']
    if oldperson_id:
        oldperson = OldPersonInfo.query.get(oldperson_id)
        if not oldperson:
            response['code'] = "24"
            response['message'] = 'Old person information not found.'
            return response

    # 更新事件信息
    for field in EventInfo.__table__.columns:
        field_name = field.name
        if field_name in request.form and request.form[field_name]:
            setattr(event, field_name, request.form[field_name])

    db.session.commit()

    # 返回成功消息
    response['code'] = "200"
    response['message'] = 'Event information updated successfully.'
    return response


# 查询特定事件信息
@event.route('/getEvent/<int:event_id>', methods=['GET'])
def get_event(event_id):
    response = {}

    # 检查事件信息是否存在
    event = EventInfo.query.get(event_id)
    if not event:
        response['code'] = "23"
        response['message'] = 'Event information not found.'
        return response

    # 返回事件信息
    response['code'] = "200"
    response['message'] = 'Event information found.'
    response['data'] = event.to_dict()
    return response


# 查询所有事件信息（后端分页查询）
@event.route('/getAllEvents', methods=['GET'])
def get_all_events():
    response = {}

    # 获取分页参数
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    # 计算跳过的条目数量
    offset = (page - 1) * per_page

    # 查询事件信息
    events = EventInfo.query.offset(offset).limit(per_page).all()

    # 查询总条目数
    total_items = EventInfo.query.count()

    # 计算总页数
    total_pages = int(math.ceil(total_items / per_page))

    # 构造分页结果
    event_list = [event.to_dict() for event in events]

    # 返回分页结果
    response['code'] = "200"
    response['message'] = 'Event information retrieved successfully.'
    response['data'] = {
        'items': event_list,
        'total_pages': total_pages,
        'total_items': total_items
    }
    return response
