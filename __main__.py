#coding: utf-8
"""
Quickly host files on a local web server.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time
import tkinter as tk
from tkinter import filedialog

__version__ = "1.2"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

server_up = False

def exe_dir():
    """Return the executable directory."""
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
    elif __file__:
        exe_path = os.path.dirname(__file__)
    return exe_path

def browse_dir():
    """Return the path to the directory of your choice."""
    window.filename = filedialog.askdirectory(initialdir=exe_dir())
    ent_folder.delete(0, tk.END)
    ent_folder.insert(0, window.filename)
    os.chdir(window.filename)
    return window.filename

def init_server():
    """Start a local web server. Use port 8000 or higher."""
    global port
    port = 7999
    while True:
        try:
            port +=1
            global httpd
            httpd = socketserver.TCPServer(("localhost", port), http.server.SimpleHTTPRequestHandler)
            global server_status
            server_status = f"localhost:{port} is up"
            global server_up
            server_up = True
            httpd.serve_forever()
            break
        except:
            continue

def start_server():
    """Host the files from the entry field folder on a local web server and use port 8000 or higher. Update the GUI, and if the checkbutton is selected, open the server address in a default web browser."""
    try:
        os.chdir(ent_folder.get())
    except FileNotFoundError:
        lbl_error.config(text=f"❗directory does not exist")
    else:
        lbl_error.config(text="")
        t1 = threading.Thread(target=init_server, daemon=True)
        t1.start()
        while not server_up:
            time.sleep(1)
        lbl_status.config(text=f"✔️{server_status}")
        btn_start.config(state="disabled", command="")
        btn_stop.config(state="normal", command=kill_server)
        if preview.get() == 1:
            webbrowser.open(url=f"http://localhost:{str(port)}", new=1, autoraise=True)  

def kill_server():
    """Kill the started local web server and update the GUI."""
    httpd.shutdown()
    global server_up
    server_up = False
    lbl_status.config(text=f"🟥 server stopped")
    btn_start.config(state="normal", command=start_server)
    btn_stop.config(state="disabled", command="")

window = tk.Tk()
window.title("Hosty")
window.columnconfigure([0], minsize=150, weight=1)
window.rowconfigure([1, 2], weight=1)

frm_input = tk.Frame(master=window)
input_lbl = tk.Label(text="📁 Directory to host ", font="default 14 bold", master=frm_input)
btn_browse = tk.Button(text="Browse...", master=frm_input, command=browse_dir)
ent_folder = tk.Entry(width="60", master=frm_input)

frm_controls = tk.Frame(master=window)
btn_start = tk.Button(text="Start Server", height="2", font="default 14 bold", borderwidth="4", command=start_server, master=frm_controls)
btn_stop = tk.Button(text="Stop Server", height="2", font="default 14 bold", borderwidth="4", state="disabled", master=frm_controls)

frm_status = tk.Frame(master=window)
preview = tk.IntVar()
chkbtn_preview = tk.Checkbutton(text="Web browser preview", variable=preview, onvalue=1, master=frm_status)
chkbtn_preview.select()
lbl_error = tk.Label(font="TkFixedFont", master=frm_status)
lbl_status = tk.Label(text=f"❌ server not running", font="TkFixedFont", master=frm_status)

frm_input.grid(row=0, column=0, padx="10", pady="10", sticky="we")
input_lbl.pack(side=tk.LEFT)
ent_folder.pack(side=tk.LEFT, fill=tk.X, expand=True)
btn_browse.pack(side=tk.LEFT)

frm_controls.grid(row=1, column=0, padx="10", pady="10", sticky="ns")
btn_start.pack(side=tk.LEFT)
btn_stop.pack(side=tk.LEFT)

frm_status.grid(row=3, column=0, sticky="we", padx="10", pady="10")
chkbtn_preview.pack(side=tk.LEFT)
lbl_status.pack(side=tk.RIGHT)
lbl_error.pack(side=tk.RIGHT)

def main():
    ent_folder.insert(0, exe_dir())
    # os.chdir("../../../") # Uncomment for building macOS apps.
    window.mainloop()

if __name__ == '__main__':
    main()