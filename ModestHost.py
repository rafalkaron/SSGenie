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
    os.chdir(app_path)
    if os.name=="posix":
        os.chdir("../../../") # Needed if you want to compile this as a macOS bundle/app.
    t1 = threading.Thread(target=start_server)
    t2 = threading.Thread(target=open_default_localhost)

    t1.start()
    while PORT is None:
        time.sleep(1)
    t2.start()
    t2.join()
    t1.join()

    
if __name__ == '__main__':
    main()