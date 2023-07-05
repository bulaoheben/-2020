from app.mod_employee.models import Employee


def get_all_employee():
    return Employee.query.all()


def select_by_id(id) -> Employee:
    return Employee.query.get(id)

