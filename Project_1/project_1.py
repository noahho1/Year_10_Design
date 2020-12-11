import tkinter as tk
import requests
import json

uNames = ["user1@test.com", "user2@test.com"]
pWords = ["pword1", "pword2"]
ttables = ["1", "2", "3", "4"]

def checkCred(*arg):

#THIS IS HOW TO SWITCH FRAMES
	loginFrame.pack_forget()
	homeFrame.pack()



root = tk.Tk() #Creates your main window

#Build a login frame
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
variable.set(ttables[0]) # default value - Set to Canadian

ttable_select = tk.OptionMenu(f1, variable, *ttables)

ttable_label.pack()
ttable_select.pack()

#Frame 2 Setup

pans_label = tk.Label(f2, text = "Past Answers")
pans2_label = tk.Label(f2, text = "Select a past question to view your answer")

pans_label.pack()
pans2_label.pack()
#Frame 3 Setup

prac_label = tk.Label(f3, text = "Practice")
prac2_label = tk.Label(f3, text = "Practice your times tables here!")
que_label = tk.Label(f3, text = "Question")
ansent = tk.Entry(f3)
sub_button = tk.Button(f3)

prac_label.pack()
prac2_label.pack()
que_label.pack()
ansent.pack()
sub_button.pack()

display = tk.Label(f3, height = 25, width = 60, text = " ")
display.pack()



f1.grid(row = 0, column = 0, sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)
f2.grid(row = 1, column = 0, sticky = "NESW", padx = 5, pady= 5, ipadx = 2, ipady = 2)
f3.grid(row = 0, column = 1, rowspan = 2, columnspan = 2, sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)



loginFrame.pack()
root.mainloop()


