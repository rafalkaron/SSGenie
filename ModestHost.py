#coding: utf-8
"""
    ModestHost
    *********************************************************
    Quickly host files from the ModestHost directory.

    *********************************************************
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

__version__ = "0.9"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

address = "localhost"
PORT = None

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
elif __file__:
    app_path = os.path.dirname(__file__)

def start_server():
    global info_starting_server
    info_starting_server = print("Trying to host files from " + app_path + " on:")
    global PORT
    PORT = 7999
    while True:
        try:
            PORT +=1
            server()
            break
        except:
            continue
        else:
            print("Cannot host files on localhost. Reboot your workstation and try again.")
        break

def server():
    print(" - " + address +":" +str(PORT))
    global httpd
    httpd = socketserver.TCPServer((address, PORT), http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()
    

def open_default_localhost():
    print("Opening " + address + ":" + str(PORT) + " in your default web browser")
    webbrowser.open(url="http://" + address +":"+str(PORT), new=1, autoraise=True)

def main():
    if os.name=="nt":
        os.chdir(app_path)
    if os.name=="posix":
        _script_filepath = os.path.abspath(__file__)
        _script_filename = os.path.basename(__file__)
        _script_directory = _script_filepath.replace(_script_filename, "").replace("\\", "/")
        os.chdir(_script_directory)
        os.chdir("../../../")
    t1 = threading.Thread(name="daemon", target=start_server, daemon=True)
    t2 = threading.Thread(name="non-daemon", target=open_default_localhost)

    t1.start()
    while PORT is None:
        time.sleep(1)
    t2.start()
    t1.join()
    t2.join()
 
if __name__ == '__main__':
    main()