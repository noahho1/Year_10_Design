import tkinter as tk
import requests
import json


root = tk.Tk()

f1 = tk.Frame(highlightbackground = "black", highlightthickness=1)
f2 = tk.Frame(highlightbackground = "black", highlightthickness=1)
f3 = tk.Frame(highlightbackground = "black", highlightthickness=1)



cur_label = tk.Label(f1, text = "Hello World")


cur_label.pack()




input1_label = tk.Label(f2, text = "Text")
input2_label = tk.Label(f2, text = "Lorem Ipsum")


input1_label.pack()
input2_label.pack()


info_btn1 = tk.Button(f3, text = "Button", width = 10)


info_btn1.pack(side = tk.LEFT)


f1.grid(row = 0, column = 0, sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)
f2.grid(row = 1, column = 0, sticky = "NESW", padx = 5, pady= 5, ipadx = 2, ipady = 2)
f3.grid(row = 0, column = 1, rowspan = 2,sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)





root.mainloop()
root.mainloop()