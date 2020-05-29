# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import tkinter as tk

window = tk.Tk()

window.columnconfigure([0], minsize=250)
window.rowconfigure([0, 1, 2, 3], minsize=25)

input_lbl = tk.Label(text="Enter the directory that contains the files that you want to host")
input_lbl.grid(row=0, column=0)
ent_folder = tk.Entry()
ent_folder.grid(row=1, column=0)
btn_start = tk.Button(text="Start Server", height="2")
btn_start.grid(row=2, column=0)
btn_stop = tk.Button(text="Stop Server", height="2")
btn_stop.grid(row=3, column=0)
status_lbl = tk.Label(text="localhost:8000 is up")
status_lbl.grid(row=4, column=0)

window.mainloop()

"""
frm_input = tk.Frame(width=200, bg="green", master=window)
frm_input.pack(fill=tk.BOTH, expand =True)

frm_controls = tk.Frame(width=200, bg="red", master=window)
frm_controls.pack()

frm_status = tk.Frame(width=200, bg="blue", master=window)
frm_status.pack(fill=tk.X)


input_lbl = tk.Label(text="Enter the directory that contains the files that you want to host", height="2", master=frm_input)
input_lbl.pack()
ent_folder = tk.Entry(master=frm_input)
ent_folder.pack(fill=tk.X)
ent_folder_retrive = ent_folder.get()
btn_start = tk.Button(text="Start Server", height="2", master=frm_controls)
btn_start.pack(side=tk.LEFT)
btn_stop = tk.Button(text="Stop Server", height="2", master=frm_controls)
btn_stop.pack(side=tk.RIGHT)
status = "localhost:8000 is up"
status_lbl = tk.Label(text=f"Status: {status}", master=frm_status)
status_lbl.pack(side=tk.LEFT)
"""
window.mainloop()