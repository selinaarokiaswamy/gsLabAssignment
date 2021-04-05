from employee import app
from employee.models import db


def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

from employee import routes

