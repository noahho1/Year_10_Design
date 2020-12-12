import tkinter as tk
import requests
import json
from pprint import pprint
import random

resp = requests.get("https://raw.githubusercontent.com/noahho1/Year_10_Design/master/Project_1/data.json")
data = resp.json()

questions = []
answers = []
ttables = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
panswer = [" "]
pdata = [0,"user1",0,0]

#uNames = ["user1@test.com", "user2@test.com"]
#pWords = ["pword1", "pword2"]

#TAKING DATA FROM JSON FILE AND PUTTING IN LISTS QUESTIONS AND ANSWERS FOR USE IN PROGRAM
for i in range(0, len(data),1):
	questions.append(data[i]["question"])
	answers.append(data[i]["answer"])

def checkCred(*arg):

#THIS IS HOW TO SWITCH FRAMES
	loginFrame.pack_forget()
	homeFrame.pack()

#CHANGE Q IF ANSWER IS CORRECT
def next(*args):
	ans = ansent.get()
	cq = pdata[0]
	if (ans == answers[cq]):
		labelR.config(text = "Correct")
		x = random.randint(0, len(questions) -1)
		que_label.config(text = questions[x])
	else:
		labelR.config(text = "Wrong")

root = tk.Tk() 

#Builds a login frame
loginFrame = tk.Frame(root)

flogin = tk.Frame(loginFrame, highlightbackground = "green", highlightthickness=5)

labunLF = tk.Label(flogin,text = "User Name:",)
entunLF = tk.Entry(flogin, width = 20, highlightbackground = "cyan", highlightthickness=2.5 )

labpwLF = tk.Label(flogin,text = "Password", )
entpwLF = tk.Entry(flogin, width = 20, highlightbackground = "cyan", highlightthickness=2.5 )

submitLF = tk.Button(flogin, text = "Submit", command = checkCred)


labunLF.pack()
entunLF.pack()

labpwLF.pack()
entpwLF.pack()

submitLF.pack()

flogin.grid(padx = 5, pady = 5)

#Build a home page frame
homeFrame = tk.Frame(root)
homeFrame.config(bg = "green")

f1 = tk.Frame(homeFrame, highlightbackground = "cyan", highlightthickness=5)
f2 = tk.Frame(homeFrame, highlightbackground = "cyan", highlightthickness=5)
f3 = tk.Frame(homeFrame, highlightbackground = "cyan", highlightthickness=5)

#Frame 1 Setup
ttable_label = tk.Label(f1, text = "Select Times Table")
variable = tk.StringVar(root)
variable.set(ttables[0]) 

ttable_select = tk.OptionMenu(f1, variable, *ttables)

ttable_label.pack()
ttable_select.pack()

#Frame 2 Setup

pans_label = tk.Label(f2, text = "Past Answers")
pans2_label = tk.Label(f2, text = "Select a past question to view your answer")
variable1 = tk.StringVar(root)
variable1.set(panswer[0]) 

pans_select = tk.OptionMenu(f2, variable1, *panswer)


pans_label.pack()
pans2_label.pack()
pans_select.pack()
#Frame 3 Setup

prac_label = tk.Label(f3, text = "Practice")
prac2_label = tk.Label(f3, text = "Practice your times tables here!")
que_label = tk.Label(f3, text = questions[0])
ansent = tk.Entry(f3)
labelR = tk.Label(f3,text = "ENTER AN ANSWER")
subbtn = tk.Button(f3, text = "NEXT", command = next)


prac_label.pack()
prac2_label.pack()
que_label.pack()
ansent.pack()
labelR.pack()
subbtn.pack()

display = tk.Label(f3, height = 25, width = 60, text = " ")
display.pack()



f1.grid(row = 0, column = 0, sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)
f2.grid(row = 1, column = 0, sticky = "NESW", padx = 5, pady= 5, ipadx = 2, ipady = 2)
f3.grid(row = 0, column = 1, rowspan = 2, columnspan = 2, sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)



loginFrame.pack()
root.mainloop()


