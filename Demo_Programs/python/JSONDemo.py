import requests
import json

resp = requests.get('https://jsonplaceholder.typicode.com/users')

#Converts response to JSON
data = resp.json()

#Prints out first element
print(data[0])



print(data[0]["id"])
print(data[0]["name"])



