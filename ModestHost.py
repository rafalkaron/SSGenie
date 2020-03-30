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

__version__ = "0.9.2"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

address = "localhost"
PORT = None

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
elif __file__:
    app_path = os.path.dirname(__file__)

def start_localhost():
    global info_starting_server
    info_starting_server = print("Trying to host files from " + app_path + " on:")
    global PORT
    PORT = 7999
    while True:
        try:
            PORT +=1
            print(" - " + address +":" +str(PORT))
            httpd = socketserver.TCPServer((address, PORT), http.server.SimpleHTTPRequestHandler)
            te1 = threading.Thread(print("Server alive"))
            te2 = threading.Thread(httpd.serve_forever())
            break
        except:
            continue

def server_alive():
    print("Server alive")
    global server_alive
    server_alive = True
server_alive = False

def open_default_localhost():
    print("Opening " + address + ":" + str(PORT) + " in your default web browser")
    webbrowser.open(url="http://" + address +":"+str(PORT), new=1, autoraise=True)

def main():
    os.chdir(app_path)
    if os.name=="posix":       # Uncomment for .app builds
        os.chdir("../../../")
    t1 = threading.Thread(target=start_localhost)
    t2 = threading.Thread(target=open_default_localhost)
    t1.start()
    time.sleep(5) #make it more elegant
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()