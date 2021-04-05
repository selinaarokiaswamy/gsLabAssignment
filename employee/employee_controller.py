import connexion
from employee.models import Employee
from employee import app
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)


def create():
    if connexion.request.is_json:
        body = connexion.request.get_json()
        print(body)

        Employee.add_emp(emp=body)
        return {'message': 'data saved'}, 200
    else:
        return {'message': 'data not saved'}, 400


def get():
    print('Get Records hit')
    print(Employee.query.all())
    return employees_schema.dump(Employee.query.all()), 200


def get_single_employee(id):
    print('Get Records hit')
    employee = Employee.query.filter(Employee.id == id) \
        .one_or_none()
    if employee is not None:

        # employee_schema = EmployeeSchema()
        return employee_schema.dump(employee), 200
    else:
        return {'message': 'employee not found'}, 400


def update_employee(id):
    if connexion.request.is_json:
        body = connexion.request.get_json()
        print(body)

        Employee.update_emp(emp_id=id, emp=body)
        return {'message': 'employee information saved'}, 200
    else:
        return {'message': 'employee information not saved'}, 400


def delete_employee(id):
    Employee.delete_emp(emp_id=id)
    return {'message': 'employee deleted'}, 200


def bulk_create():
    if connexion.request.is_json:
        body = connexion.request.get_json()
        print(body)

        for emp in body:
            print(emp)
            Employee.add_emp(emp=emp)
        return {'message': 'data saved'}, 200
    else:
        return {'message': 'data not saved'}, 400


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "designation", "department", "phoneNo")

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("emp_detail", values=dict(id="<id>")),
            "collection": ma.URLFor("employees"),
        }
    )


employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)