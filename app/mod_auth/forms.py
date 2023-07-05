from flask import request, render_template, redirect, url_for, Blueprint, jsonify
import app.mod_user.controllers as user_c
from app import app
from app import db

app02 = Blueprint('user', __name__)


# 登录接口
@app.route('/login', methods=['GET', 'POST'])
def do_login_do():
    if request.method == 'GET':
        return render_template("login.html")

    username = request.form['username']
    password = request.form['password']
    user = user_c.select_by_password(username, password)

    if user:
        return redirect(url_for('index.html'))


# 查询所有管理员用户接口, 返回json信息
@app.route('/userList')
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


# 编辑管理员信息，需要传入管理员id进行查询，并在body中携带数据
@app.route('/editUser/<int:id>', methods=['POST'])
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

