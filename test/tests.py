import requests
from data import messages_add, messages_get, users_add, chats_add, chats_get
# curl --header "Content-Type: application/json" --request POST --data \
# "{\"username\": \"user_2\"}" http://localhost:9000/users/add
#
# curl --header "Content-Type: application/json" --request POST --data \
#  "{\"name\": \"chat_2\", \"users\": [\"1\", \"3\"]}"\
#  http://localhost:9000/chats/add
#
# curl --header "Content-Type: application/json" --request POST --data\
#  "{\"chat\": \"1\", \"author\": \"1\", \"text\": \"hi\"}"\
#  http://localhost:9000/messages/add
#
# curl --header "Content-Type: application/json" --request POST --data \
# "{\"chat\": \"1\"}" http://localhost:9000/messages/get
#
# curl --header "Content-Type: application/json" --request POST --data\
#  "{\"user\": \"1\"}" http://localhost:9000/chats/get


for i in users_add:
    a = requests.post(
                        "http://localhost:9000/users/add",
                        headers={"Content-Type": "application/json"},
                        json=i
                    )

    print(a.text, a.status_code)

for i in chats_add:
    a = requests.post(
                        "http://localhost:9000/chats/add",
                        headers={"Content-Type": "application/json"},
                        json=i
                    )

    print(a.text, a.status_code)

for i in chats_get:
    a = requests.post(
                    "http://localhost:9000/chats/get",
                    headers={"Content-Type": "application/json"},
                    json=i)
    print(a.text, a.status_code)

for i in messages_add:
    a = requests.post(
                        "http://localhost:9000/messages/add",
                        headers={"Content-Type": "application/json"},
                        json=i
                    )
    print(a.text, a.status_code)

for i in messages_get:
    a = requests.post(
                    "http://localhost:9000/messages/get",
                    headers={"Content-Type": "application/json"},
                    json=i
                )
    print(a.text, a.status_code)
