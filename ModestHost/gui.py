# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import tkinter as tk

window = tk.Tk()

frame_input = tk.Frame(master=window)
frame_controls = tk.Frame(master=window)
frame_status = tk.Frame(master=window)

input_label = tk.Label(text="Enter the directory that contains the files that you want to host", height="2", master=frame_input)
input_label.pack()
entry_folder = tk.Entry(width="60", master=frame_input)
entry_folder.pack()
entry_folder_retrive = entry_folder.get()

button_start = tk.Button(text="Start Server", height="2", master=frame_controls)
button_start.pack(side=tk.LEFT)
button_stop = tk.Button(text="Stop Server", height="2", master=frame_controls)
button_stop.pack(side=tk.RIGHT)

status = "localhost:8000 is up"

status_label = tk.Label(text=f"Status: {status}", master=frame_status)
status_label.pack()

frame_input.pack()
frame_controls.pack()
frame_status.pack(side=tk.LEFT)

window.mainloop()