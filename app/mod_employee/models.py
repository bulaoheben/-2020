from app import db


class Employee(db.Model):
    __tablename__ = 'employee_info'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=True)  # 工作人员姓名
    gender = db.Column(db.String(5), nullable=True)  # 性别
    phone = db.Column(db.String(50), nullable=True)  # 电话
    id_card = db.Column(db.String(50), nullable=True)  # 身份证号
    birthday = db.Column(db.DateTime, nullable=True)  # 出生日期
    hire_date = db.Column(db.DateTime, nullable=True)  # 入职日期
    resign_date = db.Column(db.DateTime, nullable=True)  # 离职日期
    imgset_dir = db.Column(db.String(200), nullable=True)  # 图像目录
    profile_photo = db.Column(db.String(200), nullable=True)  # 头像路径
    description = db.Column(db.String(200), nullable=True)  # 描述
    isactive = db.Column(db.String(10), nullable=True)  # 是否有效
    created = db.Column(db.DateTime, nullable=True)  # 创建时间
    updated = db.Column(db.DateTime, nullable=True)  # 更新时间


    def to_dict(self):
        if self.birthday:
            birthday = self.birthday.strftime("%Y-%m-%d")
        else:
            birthday = self.birthday
        if self.hire_date:
            hire_date = self.hire_date.strftime("%Y-%m-%d")
        else:
            hire_date = self.hire_date
        if self.resign_date:
            resign_date = self.resign_date.strftime("%Y-%m-%d")
        else:
            resign_date = self.resign_date
        if self.created:
            created = self.created.strftime("%Y-%m-%d %H:%M:%S")
        else:
            created = self.created
        if self.updated:
            updated = self.updated.strftime("%Y-%m-%d %H:%M:%S")
        else:
            updated = self.updated

        return {
            'id': self.id,
            'username': self.username,
            'gender': self.gender,
            'phone': self.phone,
            'id_card': self.id_card,
            'birthday': birthday,
            'hire_date': hire_date,
            'resign_date': resign_date,
            'imgset_dir': self.imgset_dir,
            'profile_photo': self.profile_photo,
            'description': self.description,
            'isactive': self.isactive,
            'created': created,
            'updated': updated,
        }

