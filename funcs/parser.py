from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument(
                    'username',
                    help="Упс, что-то пошло не так!",
                    location='json'
                )
parser.add_argument('name', location='json')
parser.add_argument('users', type=list, location='json')
parser.add_argument('chat', location='json')
parser.add_argument('author', location='json')
parser.add_argument('text', location='json')
parser.add_argument("user", location='json')
