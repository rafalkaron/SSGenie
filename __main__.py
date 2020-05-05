#coding: utf-8
"""
Quickly host files from the ModestHost directory.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

__version__ = "1.0"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

address = "localhost"
PORT = None
server_alive = False
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
            global httpd
            httpd = socketserver.TCPServer((address, PORT), http.server.SimpleHTTPRequestHandler)
            print("Server alive")
            global server_alive
            server_alive = True
            httpd.serve_forever()
            break
        except:
            continue

def open_default_localhost():
    print("Opening " + address + ":" + str(PORT) + " in your default web browser")
    webbrowser.open(url="http://" + address +":"+str(PORT), new=1, autoraise=True)    

def main():
    os.chdir(app_path)
    if os.name=="posix":    # Uncomment for macOS .app builds
        os.chdir("../../../")
    t1 = threading.Thread(target=start_localhost)
    t2 = threading.Thread(target=open_default_localhost)
    t1.start()
    while server_alive == False:    # This is busy-waiting - think how to improve this
        print("Waiting for localhost...")
        time.sleep(1)
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()