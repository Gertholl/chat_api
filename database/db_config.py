from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.sqlite'
    db.init_app(app)
    return app

__all__ = ["db", "create_app"]