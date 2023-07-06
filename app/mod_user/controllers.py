from app.mod_user.models import User


def get_all_user():
    return User.query.all()


def select_by_id(id) -> User:
    return User.query.get(id)


def select_by_password(name, password):
    return User.query.filter_by(username=name, password=password).first()


def select_by_username(username):
    return User.query.filter_by(username=username).first()
