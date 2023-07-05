from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'sys_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)  # 用户名
    password = db.Column(db.String(50), nullable=True)  # 密码
    real_name = db.Column(db.String(50), nullable=True)  # 真实姓名
    sex = db.Column(db.String(20), nullable=True)  # 性别
    email = db.Column(db.String(50), nullable=True)  # 邮箱
    phone = db.Column(db.String(50), nullable=True)  # 电话
    mobile = db.Column(db.String(50), nullable=True)  # 移动电话
    description = db.Column(db.String(200), nullable=True)  # 描述
    isactive = db.Column(db.String(10), nullable=True)  # 是否有效
    created = db.Column(db.DateTime, nullable=True)  # 创建时间
    createby = db.Column(db.Integer, nullable=True)  # 创建人
    updated = db.Column(db.DateTime, nullable=True)  # 更新时间
    updateby = db.Column(db.Integer, nullable=True)  # 更新人
    remove = db.Column(db.String(1), nullable=True)  # 是否删除
    datafilter = db.Column(db.String(200), nullable=True)  # 数据过滤
    theme = db.Column(db.String(45), nullable=True)  # 主题
    defaultpage = db.Column(db.String(45), nullable=True)  # 登录成功页面
    logoimage = db.Column(db.String(45), nullable=True)  # 显示不同logo
    qqopenid = db.Column(db.String(100), nullable=True)  # 第三方登录的凭证
    appversion = db.Column(db.String(10), nullable=True)  # 检测app的版本号
    jsonauth = db.Column(db.String(1000), nullable=True)  # app权限控制

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'real_name': self.real_name,
            'sex': self.sex,
            'email': self.email,
            'phone': self.phone,
            'mobile': self.mobile,
            'description': self.description,
            'isactive': self.isactive,
            'created': self.created,
            'createby': self.createby,
            'updated': self.updated,
            'updateby': self.updateby,
            'remove': self.remove,
            'datafilter': self.datafilter,
            'theme': self.theme,
            'defaultpage': self.defaultpage,
            'logoimage': self.logoimage,
            'qqopenid': self.qqopenid,
            'appversion': self.appversion,
            'jsonauth': self.jsonauth
        }

