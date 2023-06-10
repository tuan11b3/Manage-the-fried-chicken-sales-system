import json
import requests


todo = {"username":"tk", "password": "123"}
chUser_Url = "https://apichicken.herokuapp.com/api/login/"
response = requests.post(chUser_Url, todo)
data = response.json()
print(data)
