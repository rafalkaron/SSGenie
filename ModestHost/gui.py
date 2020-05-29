# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import tkinter as tk

window = tk.Tk()

window.columnconfigure([0], minsize=150, weight=1)
window.rowconfigure([1, 3], minsize=0, weight=1)

frm_input = tk.Frame(master=window)
frm_input.grid(row=0, column=0, padx="10", pady="10", sticky="w")
input_lbl = tk.Label(text="Directory to host:", master=frm_input)
input_lbl.pack(side=tk.LEFT)
ent_folder = tk.Entry(width="60", master=frm_input)
ent_folder.pack(fill=tk.X)

frm_controls = tk.Frame(master=window)
frm_controls.grid(row=1, column=0, padx="10", pady="10", sticky="n")
chkbtn_preview = tk.Checkbutton(text="Open in browser", master=frm_controls)
chkbtn_preview.pack()
btn_start = tk.Button(text="Start Server", height="2", master=frm_controls)
btn_start.pack(side=tk.LEFT)
btn_stop = tk.Button(text="Stop Server", height="2", master=frm_controls)
btn_stop.pack(side=tk.LEFT)

frm_status = tk.Frame(master=window)
frm_status.grid(row=3, column=0, sticky="ws", padx="10", pady="10")
lbl_status = tk.Label(text="Status:", master=frm_status)
lbl_status.pack(side=tk.LEFT)
lbl_status_variable = tk.Label(text="localhost:8000 is up", master=frm_status)
lbl_status_variable.pack(side=tk.LEFT)

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
lbl_status = tk.Label(text=f"Status: {status}", master=frm_status)
lbl_status.pack(side=tk.LEFT)
"""
window.mainloop()