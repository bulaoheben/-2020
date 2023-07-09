from app import db


class OldPersonInfo(db.Model):
    __tablename__ = 'oldperson_info'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=True)  # 用户名
    gender = db.Column(db.String(10), nullable=True)  # 性别
    phone = db.Column(db.String(50), nullable=True)
    id_card = db.Column(db.String(50), nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    checkin_date = db.Column(db.DateTime, nullable=True)
    checkout_date = db.Column(db.DateTime, nullable=True)
    imgset_dir = db.Column(db.String(200), nullable=True)
    profile_photo = db.Column(db.String(200), nullable=True)
    room_number = db.Column(db.String(50), nullable=True)
    firstguardian_name = db.Column(db.String(50), nullable=True)
    firstguardian_relationship = db.Column(db.String(50), nullable=True)
    firstguardian_phone = db.Column(db.String(50), nullable=True)
    firstguardian_wechat = db.Column(db.String(50), nullable=True)
    secondguardian_name = db.Column(db.String(50), nullable=True)
    secondguardian_relationship = db.Column(db.String(50), nullable=True)
    secondguardian_phone = db.Column(db.String(50), nullable=True)
    secondguardian_wechat = db.Column(db.String(50), nullable=True)
    health_state = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    isactive = db.Column(db.String(10), nullable=True)
    created = db.Column(db.DateTime, nullable=True)
    createby = db.Column(db.Integer, nullable=True)
    updated = db.Column(db.DateTime, nullable=True)
    updateby = db.Column(db.Integer, nullable=True)
    remove = db.Column(db.String(1), nullable=True)

    def to_dict(self):
        return {
            'ID': self.id,
            'username': self.username,
            'gender': self.gender,
            'phone': self.phone,
            'id_card': self.id_card,
            'birthday': self.birthday,
            'checkin_date': self.checkin_date,
            'checkout_date': self.checkout_date,
            'imgset_dir': self.imgset_dir,
            'profile_photo': self.profile_photo,
            'room_number': self.room_number,
            'firstguardian_name': self.firstguardian_name,
            'firstguardian_relationship': self.firstguardian_relationship,
            'firstguardian_phone': self.firstguardian_phone,
            'firstguardian_wechat': self.firstguardian_wechat,
            'secondguardian_name': self.secondguardian_name,
            'secondguardian_relationship': self.secondguardian_relationship,
            'secondguardian_phone': self.secondguardian_phone,
            'secondguardian_wechat': self.secondguardian_wechat,
            'health_state': self.health_state,
            'description': self.description,
            'isactive': self.isactive,
            'created': self.created,
            'createby': self.createby,
            'updated': self.updated,
            'updateby': self.updateby,
            'remove': self.remove
        }
