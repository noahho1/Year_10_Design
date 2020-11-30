import tkinter as tk

uNames = ["user1@test.com", "user2@test.com"]
pWords = ["pword1", "pword2"]

#Write the code to
	#Step 1: Take entry for user name
	#Step 2: Take entry for password
	#Step 3: Loop through usernames and check if valid with password

	#If the username and password is correct swap frames. 

def checkCred(*arg):

	print("Checking")


#THIS IS HOW TO SWITCH FRAMES
	loginFrame.pack_forget()
	homeFrame.pack()

root = tk.Tk() #Creates your main window
root.geometry('400x600')
#Build a login frame
loginFrame = tk.Frame(root)

labunLF = tk.Label(loginFrame,text = "User Name:", anchor = center)
entunLF = tk.Entry(loginFrame, width = 20, anchor = center)

labpwLF = tk.Label(loginFrame,text = "Password", anchor = center)
entpwLF = tk.Entry(loginFrame, width = 20, anchor = center)

submitLF = tk.Button(loginFrame, text = "Submit", command = checkCred, anchor = center)

labunLF.pack()
entunLF.pack()

labpwLF.pack()
entpwLF.pack()

submitLF.pack()

#Build a home page frame
homeFrame = tk.Frame(root)

labHF = tk.Label(homeFrame, text = "Welcome!")

labHF.pack()



loginFrame.pack()
root.mainloop()


