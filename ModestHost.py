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
        break

def server():
    print(" - " + address +":" +str(PORT))
    httpd = socketserver.TCPServer((address, PORT), http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()

def open_default_localhost():
    time.sleep(1) # This won't be needed once I rework the loop
    print("Opening " + address + ":" + str(PORT) + " in your default web browser")
    webbrowser.open(url="http://" + address +":"+str(PORT), new=1, autoraise=True)

def main():
    os.chdir(app_path)
    if os.name=="posix":
        os.chdir("../../../") # This is for app bundle
    t1 = threading.Thread(target=start_server)
    t1.start()
    open_default_localhost()
main()