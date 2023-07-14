from app.mod_employee.models import Employee
from app.mod_oldperson.models import OldPersonInfo
from app.mod_volunteer.models import Volunteer


# 根据传入的人名列表，查询他们分别对应的身份信息
def namesToRoles(names):
    role_list = []
    for name in names:
        # 查询是否为员工
        exist_employee = Employee.query.filter_by(username=name).first()
        if exist_employee:
            role_list.append("employee")
            continue

        # 查询是否为老人
        exist_old = OldPersonInfo.query.filter_by(username=name).first()
        if exist_old:
            role_list.append("old")
            continue

        # 查询是否为志愿者
        exist_volunteer = Volunteer.query.filter_by(name=name).first()
        if exist_volunteer:
            role_list.append("volunteer")
            continue

        # 判定为陌生人
        role_list.append("stranger")

    return role_list


# 根据老人的姓名，查询该老人的id
def find_old_id_by_name(name):
    old_info = OldPersonInfo.query.filter_by(username=name).first()
    return old_info.id


# 根据义工的姓名，查询其id
def find_volunteer_id_by_name(name):
    return Volunteer.query.filter_by(name=name).first()


if __name__ == '__main__':
    print(namesToRoles(["1", "2"]))
