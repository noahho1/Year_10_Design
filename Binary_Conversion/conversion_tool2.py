import tkinter as tk

print("Stage 2")


def process(*args):
	print("process")

	val = ent_value.get()
	print(val)




	ent_value.delete(0,tk.END) 

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