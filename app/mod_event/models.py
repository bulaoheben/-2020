from app import db


class EventInfo(db.Model):
    __tablename__ = 'event_info'

    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.Integer)
    event_date = db.Column(db.DateTime)
    event_location = db.Column(db.String(200))
    event_desc = db.Column(db.String(200))
    oldperson_id = db.Column(db.Integer)
    pic_url = db.Column(db.String(100))

    def EventInfo(self, event_type, event_date, event_location, event_desc, oldperson_id, pic_url):
        self.event_type = event_type
        self.event_date = event_date
        self.event_location = event_location
        self.event_desc = event_desc
        self.oldperson_id = oldperson_id
        self.pic_url = pic_url

    def to_dict(self):
        return {
            'id': self.id,
            'event_type': self.event_type,
            'event_date': self.event_date.strftime('%Y-%m-%d %H:%M:%S') if self.event_date else None,
            'event_location': self.event_location,
            'event_desc': self.event_desc,
            'oldperson_id': self.oldperson_id,
            'pic_url': self.pic_url
        }
