from database.models import *
from flask_restful import Resource
from app import db
from funcs.parser import parser
from flask import jsonify


class UsersAdd(Resource):
    def post(self):
        args = parser.parse_args()
        user = User(username=args["username"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"id":user.id, 'created_at': user.created_at})

class ChatsAdd(Resource):
    def post(self):
        args = parser.parse_args()
        new_chat = Chat(name=args['name'])
        db.session.add(new_chat)
        db.session.commit()
        for user in args['users']:
            chat = ChatUsers(chat_id=new_chat.id, user_id=user)
            db.session.add(chat)
        db.session.commit()
        return jsonify({"id":new_chat.id, "created_at": new_chat.created_at})

class ChatsGet(Resource):
    def post(self):
        args = parser.parse_args()
        names = ["chat_id", "name", "users", "created_at"]
        resp = []
        chats = Chat.query.join(ChatUsers, ChatUsers.user_id==args['user'])\
                .filter(Chat.id==ChatUsers.chat_id).all()
        for chat in chats:
            data = str(chat).split(";")
            resp.append(dict(zip(names, data)))
        return resp

class MessagesAdd(Resource):
    def post(self):
        args=parser.parse_args()
        msg = Message(chat=args['chat'],author=args['author'],text=args['text'])
        db.session.add(msg)
        db.session.commit()
        return jsonify({"message_id": msg.id})

class MessagesGet(Resource):
    def post(self):
        args = parser.parse_args()
        messages = Message.query.join(ChatUsers, ChatUsers.chat_id==args['chat']).filter(Message.chat == ChatUsers.chat_id).all()
        names = ["message_id", "chat_id", "autor", "text", "created_at"]
        response = []
        for message in messages:
            data = str(message).split(";")
            response.append(dict(zip(names, data)))
        return response


__all__ = ['UsersAdd','ChatsAdd','MessagesAdd','MessagesGet','ChatsGet']