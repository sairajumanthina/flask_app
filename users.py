import json
import requests

def return_users_data():
    response=requests.get("https://reqres.in/api/users?page=1")
    response_body=json.loads(response.text)
    users=response_body["data"]
    print(users)
    return users