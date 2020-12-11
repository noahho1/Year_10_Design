import requests
import json
from pprint import pprint
import tkinter as tk

#Get Key
#This is a file not in my respository I don't want you to have it
file = open("..//..//API_Keys//fixerkey.txt","r")

key = file.read()


resp = requests.get('http://data.fixer.io/api/latest?access_key='+key)
#resp = requests.get('https://jsonplaceholder.typicode.com/comments')


#Converts response to JSON
data = resp.json()

'''
pprint(data)
print(data["rates"]["CAD"])
'''

country = []
value = []

for key in data["rates"]:
	print(key,":",data["rates"][key])
	country.append(key)
	value.append(data["rates"][key])

print(country)
print(value)

def change(x):
	print(x)
	
root = tk.Tk()

lab = tk.Label(root, text = "Select Currency")

var = tk.StringVar(root)
var.set(country[27])
option_menu = tk.OptionMenu(root, var, *country, command = change)

lab.pack()
option_menu.pack()

root.mainloop()
print("END")