from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Employee(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    designation = db.Column(db.String(length=30))
    department = db.Column(db.String(length=20))
    phoneNo = db.Column(db.Integer())

    def add_emp(emp):
        e = Employee(name=emp['name'],
                     department=emp['department'],
                     designation=emp['designation'],
                     phoneNo=emp['phoneNo'])
        db.session.add(e)
        db.session.commit()


    def update_emp(emp_id,emp):
        e = Employee.query.get(emp_id)
        e.name = emp['name']
        e.department = emp['department']
        e.designation = emp['designation']
        e.phoneNo = emp['phoneNo']
        db.session.commit()

    def delete_emp(emp_id):
        Employee.query.filter_by(id=emp_id).delete()
        db.session.commit()


