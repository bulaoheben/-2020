from app.mod_employee.models import Employee


def get_all_employee():
    return Employee.query.all()


def select_by_id(id) -> Employee:
    return Employee.query.get(id)


def get_valid_employee() -> Employee:
    return Employee.query.filter_by(resign_date=None)
