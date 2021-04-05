from flask import Flask
import connexion
from flask_sqlalchemy import SQLAlchemy

connexion_app = connexion.App(__name__, specification_dir='./')
app = connexion_app.app
connexion_app.add_api('swagger.yml')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gsLabEmployee.db'
db = SQLAlchemy(app)
