from urllib import response
import requests

response = requests.get('http://127.0.0.1:8000/jokes')
print(response.json())