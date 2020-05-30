#coding: utf-8
"""
Quickly host files from the ModestHost directory on a localhost web server.
"""
# Compile by using PyInstaller with the --onedir argument. Then, in Platypus, add the compiled files to the bundle, use the "run.sh" file as the script, and select the "Remain running after execution" option.
import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import multiprocessing
import time
import tkinter as tk

__version__ = "1.2"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

server_status = "No web server running"
server_up = False

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
preview = tk.IntVar()
chkbtn_preview = tk.Checkbutton(text="Open in a web browser", variable=preview, onvalue=1, offvalue=0, master=frm_status)
chkbtn_preview.select()
chkbtn_preview.pack(side=tk.LEFT)
lbl_status = tk.Label(text=f"Status: {server_status}", master=frm_status)
lbl_status.pack(side=tk.RIGHT)


def exe_dir():
    """Return the executable directory."""
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
    elif __file__:
        exe_path = os.path.dirname(__file__)
    return exe_path

def start_web_server():
    """Start a local web server. Use port 8000 or higher."""
    global port
    port = 7999
    while True:
        try:
            port +=1
            httpd = socketserver.TCPServer(("localhost", port), http.server.SimpleHTTPRequestHandler)
            global server_status
            server_status = f"localhost:{port} is up"
            global server_up
            server_up = True
            httpd.serve_forever()
            break
        except:
            continue
        return server_status

def run_server(event):
    global t1
    t1 = threading.Thread(target=start_web_server, daemon=True)
    t1.start()
    while not server_up:
        time.sleep(1)
    lbl_status.config(text=f"Status: {server_status}")
    btn_start.config(state="disabled")
    if preview.get() == 1:
        open_webbrowser(url=f"http://localhost:{str(port)}")
    
def open_webbrowser(url):
    webbrowser.open(url=url, new=1, autoraise=True)

def kill_server(event):
    t1._stop

def main():
    os.chdir(exe_dir()) # Changes the directory to the executable directory.
    # os.chdir("../../../") # Uncomment for building macOS apps.
    
    btn_start.bind("<Button-1>", run_server)
    btn_stop.bind("<Button-2>", kill_server)

    window.mainloop()

if __name__ == '__main__':
    main()