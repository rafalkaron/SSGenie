# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import tkinter as tk

window = tk.Tk()

window.columnconfigure([0], minsize=150, weight=1)
window.rowconfigure([1, 2], minsize=3, weight=1)

frm_input = tk.Frame(master=window)
frm_input.grid(row=0, column=0, padx="10", pady="10", sticky="we")
input_lbl = tk.Label(text="Directory to host:", master=frm_input)
input_lbl.pack(side=tk.LEFT)
btn_browse = tk.Button(text="Browse...", master=frm_input)
btn_browse.pack(side=tk.LEFT)
ent_folder = tk.Entry(width="65", master=frm_input)
ent_folder.pack(fill=tk.X, expand=True)

frm_controls = tk.Frame(master=window)
frm_controls.grid(row=1, column=0, padx="10", pady="10", sticky="ns")
btn_start = tk.Button(text="Start Server", height="2", master=frm_controls)
btn_start.pack(side=tk.LEFT)
btn_stop = tk.Button(text="Stop Server", height="2", master=frm_controls)
btn_stop.pack(side=tk.LEFT)

frm_status = tk.Frame(master=window)
frm_status.grid(row=3, column=0, sticky="we", padx="10", pady="10")
chkbtn_preview = tk.Checkbutton(text="Open in a web browser", master=frm_status)
chkbtn_preview.select()
chkbtn_preview.pack(side=tk.LEFT)
lbl_status_variable = tk.Label(text="localhost:8000 is up", master=frm_status)
lbl_status_variable.pack(side=tk.RIGHT)
lbl_status = tk.Label(text="Status:", master=frm_status)
lbl_status.pack(side=tk.RIGHT)

def test(event):
    print("test")

btn_start.bind("<Button-1>", test)

window.mainloop()