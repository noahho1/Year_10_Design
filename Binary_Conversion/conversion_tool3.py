import tkinter as tk

print("Stage 2")


def process(*args):


	val = ent_value.get()



	check = check01(val)

	if (check == True):


		lab_results.config(text = "Valid Input")
	else:


		lab_results.config(text = "YOU BUGGIN")		

	ent_value.delete(0,tk.END) 

def check01(str):
		num_0 = str.count("0")
		num_1 = str.count("1")

		if num_0 + num_1 == len(str):
			return True
		else:
			return False

root = tk.Tk()

#Construct the widgets
lab_instructions = tk.Label(root, text = "Enter Binary")
ent_value = tk.Entry(root)
lab_results = tk.Label(root, text = "--")

#Add widgets to window
lab_instructions.pack()
ent_value.pack()
lab_results.pack()




root.bind("<Return>",process)
root.mainloop()