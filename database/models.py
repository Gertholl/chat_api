from datetime import datetime
from database.db_config import db
from flask import jsonify
from funcs.parser import parser

__all__=['Chat', "ChatUsers", "User", "Message"]

class ChatUsers(db.Model):

    __tablename__ = "chat_users"

    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __repr__(self):
        return f"{self.user_id}"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, unique=True)
    users = db.relationship("ChatUsers", backref="user")
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id};{self.name};{self.users};{self.created_at}"


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True,unique=True)
    chat = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable="False")
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable="False")
    text = db.Column(db.String, nullable="False")
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id};{self.chat};{self.author};{self.text};{self.created_at}"