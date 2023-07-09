from flask import request, Blueprint
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
@app.route('/login', methods=['POST'])
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


# 查询所有管理员用户接口，分页查询方式
@app.route('/userList', methods=['GET'])
def list_all_users():
    response = {}

    # 获取分页参数
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    # 查询管理员用户信息
    users = User.query.paginate(page=page, per_page=per_page, error_out=False)
    user_list = [user.to_dict() for user in users.items]

    # 构造分页结果
    response['code'] = "200"
    response["message"] = "Search success."
    response['data'] = {
        'items': user_list,
        'total_pages': users.pages,
        'total_items': users.total
    }
    return response



# 编辑管理员信息，在body中携带数据
@app.route('/editUser', methods=['PUT'])
def editUser():
    response = {}
    ID = request.args.get('id')
    targetUser = user_c.select_by_id(ID)
    if targetUser:
        if 'UserName' in request.form and request.form['UserName']:
            targetUser.username = request.form['UserName']
        if 'Password' in request.form and request.form['Password']:
            targetUser.password = request.form['Password']
        if 'REAL_NAME' in request.form and request.form['REAL_NAME']:
            targetUser.real_name = request.form['REAL_NAME']
        if 'SEX' in request.form and request.form['SEX']:
            targetUser.sex = request.form['SEX']
        if 'EMAIL' in request.form and request.form['EMAIL']:
            targetUser.email = request.form['EMAIL']
        if 'PHONE' in request.form and request.form['PHONE']:
            targetUser.phone = request.form['PHONE']
        if 'DESCRIPTION' in request.form and request.form['DESCRIPTION']:
            targetUser.description = request.form['DESCRIPTION']
        if 'ISACTIVE' in request.form and request.form['ISACTIVE']:
            targetUser.isactive = request.form['ISACTIVE']
        if 'CREATED' in request.form and request.form['CREATED']:
            targetUser.created = request.form['CREATED']
        if 'CREATEBY' in request.form and request.form['CREATEBY']:
            targetUser.createby = request.form['CREATEBY']
        if 'UPDATED' in request.form and request.form['UPDATED']:
            targetUser.updated = request.form['UPDATED']
        if 'UPDATEBY' in request.form and request.form['UPDATEBY']:
            targetUser.updateby = request.form['UPDATEBY']
        if 'REMOVE' in request.form and request.form['REMOVE']:
            targetUser.remove = request.form['REMOVE']
        if 'DATAFILTER' in request.form and request.form['DATAFILTER']:
            targetUser.datafilter = request.form['DATAFILTER']
        if 'theme' in request.form and request.form['theme']:
            targetUser.theme = request.form['theme']
        if 'defaultpage' in request.form and request.form['defaultpage']:
            targetUser.defaultpage = request.form['defaultpage']
        if 'logoimage' in request.form and request.form['logoimage']:
            targetUser.logoimage = request.form['logoimage']
        if 'qqopenid' in request.form and request.form['qqopenid']:
            targetUser.qqopenid = request.form['qqopenid']
        if 'appversion' in request.form and request.form['appversion']:
            targetUser.appversion = request.form['appversion']
        if 'jsonauth' in request.form and request.form['jsonauth']:
            targetUser.jsonauth = request.form['jsonauth']

        db.session.commit()  # 提交更新到数据库
        response['code'] = "200"
        response['message'] = 'User updated successfully.'
    else:
        response['code'] = "400"
        response['message'] = 'User not found.'

    return response


# 根据id删除对应的管理员信息
@app.route('/deleteUser', methods=['DELETE'])
def deleteUser():
    response = {}
    ID = request.args.get('id')
    targetUser = user_c.select_by_id(ID)
    if targetUser:
        db.session.delete(targetUser)
        db.session.commit()
        response['code'] = "200"
        response['message'] = 'User deleted successfully.'
    else:
        response['code'] = "400"
        response['message'] = 'User not found.'
    return response
