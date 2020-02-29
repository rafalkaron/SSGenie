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

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
elif __file__:
    app_path = os.path.dirname(__file__)

def start_server():
    print("Trying to host files from " + app_path + " on:")
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
    t1.start()
    while True:
        try:
            open_default_localhost()
        except:
            time.sleep(1)
            continue
        else:
            print("Canot open your web browser. Reboot your workstation and try again.")
        break
main()