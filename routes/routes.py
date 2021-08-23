from flask_restful import Api
from api_methods import *
from funcs.errors import errors


def init_api(app,db):
    api = Api(app, default_mediatype="application/json", errors=errors)
    api.add_resource(UsersAdd, '/users/add')
    api.add_resource(ChatsAdd, '/chats/add')
    api.add_resource(ChatsGet, '/chats/get')
    api.add_resource(MessagesAdd, '/messages/add')
    api.add_resource(MessagesGet, '/messages/get')

    return db
