from app import db

class Volunteer(db.Model):
    __tablename__ = 'volunteer_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(5))
    phone = db.Column(db.String(50))
    id_card = db.Column(db.String(50))
    birthday = db.Column(db.Date)
    checkin_date = db.Column(db.Date)
    checkout_date = db.Column(db.Date)
    imgset_dir = db.Column(db.String(200))
    profile_photo = db.Column(db.String(200))
    DESCRIPTION = db.Column(db.String(200))
    ISACTIVE = db.Column(db.String(10))
    CREATED = db.Column(db.DateTime)
    CREATEBY = db.Column(db.Integer)
    UPDATED = db.Column(db.DateTime)
    UPDATEBY = db.Column(db.Integer)
    REMOVE = db.Column(db.String(1))

    def to_dict(self):
        return {
                'id': self.id,
                'name': self.name,
                'gender': self.gender,
                'phone': self.phone,
                'id_card': self.id_card,
                'birthday': self.birthday,
                'checkin_date': self.checkin_date,
                'checkout_date': self.checkout_date,
                'imgset_dir': self.imgset_dir,
                'profile_photo': self.profile_photo,
                'DESCRIPTION': self.DESCRIPTION,
                'ISACTIVE': self.ISACTIVE,
                'CREATED': self.CREATED,
                'CREATEBY': self.CREATEBY,
                'UPDATED': self.UPDATED,
                'UPDATEBY': self.UPDATEBY,
                'REMOVE': self.REMOVE
        }

    def __init__(self, name,gender,phone,id_card,birthday,checkin_date,
                 checkout_date,imgset_dir,profile_photo,DESCRIPTION,ISACTIVE,CREATED,CREATEBY,
                 UPDATED,UPDATEBY,REMOVE):
        self.name = name
        self.gender = gender
        self.phone = phone
        self.id_card = id_card
        self.birthday = birthday
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.imgset_dir = imgset_dir
        self.profile_photo = profile_photo
        self.description = DESCRIPTION
        self.is_active = ISACTIVE
        self.created = CREATED
        self.created_by = CREATEBY
        self.updated = UPDATED
        self.updated_by = UPDATEBY
        self.remove = REMOVE

