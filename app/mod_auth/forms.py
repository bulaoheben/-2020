from flask import request, render_template, redirect, url_for, Blueprint
import app.mod_user.controllers as user_c
from app import app, db
from app.mod_user.models import User

app02 = Blueprint('user', __name__)


# 注册接口
# 需要传入的数据有UserName，Password，REAL_NAME，SEX，EMAIL，PHONE
# 根据UserName确定该用户唯一，才能够返回成功消息，否则返回失败消息
@app.route('/register', methods=['POST'])
def register():
    response = {}
    # 获取请求中的数据
    username = request.form.get('userName')
    password = request.form.get('password')
    real_name = request.form.get('realName')
    sex = request.form.get('sex')
    email = request.form.get('email')
    phone = request.form.get('phone')

    # 检查用户名是否已经存在
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        # 用户名已存在，返回失败消息
        response['code'] = "400"
        response['message'] = 'Username already exists. Please choose a different username.'
        return response

    # 创建新用户
    new_user = User(
        username=username,
        password=password,
        real_name=real_name,
        sex=sex,
        email=email,
        phone=phone
    )

    # 将新用户添加到数据库
    db.session.add(new_user)
    db.session.commit()

    # 返回成功消息
    response['code'] = "200"
    response['message'] = 'Registration successful.'
    return response


# 登录接口
@app.route('/login', methods=['GET'])
def do_login_do():
    response = {}
    username = request.form['username']
    password = request.form['password']
    user = user_c.select_by_password(username, password)

    if user:
        response["code"] = "200"
        response["message"] = "login success"
        response["data"] = user.to_dict()
        return response

    response["code"] = "400"
    response["message"] = "Incorrect username or password"
    return response


# 查询所有管理员用户接口, 返回json信息
@app.route('/userList', methods=['GET'])
def list_all_users():
    response = {}
    users = user_c.get_all_user()
    response['code'] = 200
    user_json = []
    for user in users:
        user_data = user.to_dict()
        user_json.append(user_data)
    response['data'] = user_json
    return response


# 编辑管理员信息，需要在路径中传入管理员id进行查询，并在body中携带数据
@app.route('/editUser/<int:id>', methods=['PUT'])
def editUser(id):
    response = {}
    targetUser = user_c.select_by_id(id)
    if targetUser:
        targetUser.username = request.form.get('username')
        targetUser.password = request.form.get('password')
        targetUser.real_name = request.form.get('real_name')
        targetUser.sex = request.form.get('sex')
        targetUser.email = request.form.get('email')
        targetUser.phone = request.form.get('phone')
        targetUser.mobile = request.form.get('mobile')
        targetUser.description = request.form.get('description')
        targetUser.isactive = request.form.get('isactive')
        targetUser.created = request.form.get('created')
        targetUser.createby = request.form.get('createby')
        targetUser.updated = request.form.get('updated')
        targetUser.updateby = request.form.get('updateby')
        targetUser.remove = request.form.get('remove')
        targetUser.datafilter = request.form.get('datafilter')
        targetUser.theme = request.form.get('theme')
        targetUser.defaultpage = request.form.get('defaultpage')
        targetUser.logoimage = request.form.get('logoimage')
        targetUser.qqopenid = request.form.get('qqopenid')
        targetUser.appversion = request.form.get('appversion')
        targetUser.jsonauth = request.form.get('jsonauth')

        db.session.commit()  # 提交更新到数据库
        response['code'] = 200
        response['message'] = 'User updated successfully.'
    else:
        response['code'] = 404
        response['message'] = 'User not found.'

    return response


# 根据id删除对应的管理员信息
@app.route('/deleteUser/<int:id>', methods=['DELETE'])
def deleteUser(id):
    response = {}
    targetUser = user_c.select_by_id(id)
    if targetUser:
        db.session.delete(targetUser)
        db.session.commit()
        response['code'] = 200
        response['message'] = 'User deleted successfully.'
    else:
        response['code'] = 404
        response['message'] = 'User not found.'
    return response
