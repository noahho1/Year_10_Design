import tkinter as tk

root = tk.Tk()

f1 = tk.Frame(root, highlightbackground = "black", highlightthickness=1)
f2 = tk.Frame(root, highlightbackground = "black", highlightthickness=1)
f3 = tk.Frame(root, highlightbackground = "black", highlightthickness=1)
f4 = tk.Frame(root)

#Frame 1 Setup
cur_label = tk.Label(f1, text = "Select Currency")


cur_label.pack()



#Frame 2 Setup

cur_label = tk.Label(f2, text = "Select Currency")


cur_label.pack()

#Frame 3 Setup

cur_label = tk.Label(f3, text = "Select Currency")


cur_label.pack()

display = tk.Label(f3, height = 25, width = 60, text = " ")
display.pack()



f1.grid(row = 0, column = 0, sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)
f2.grid(row = 1, column = 0, sticky = "NESW", padx = 5, pady= 5, ipadx = 2, ipady = 2)
f3.grid(row = 0, column = 1, rowspan = 2,sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)



root.mainloop()