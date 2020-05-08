#coding: utf-8
"""
Quickly host files from the current directory on a localhost:8000 (or higher) web server.
"""
### Compile this as bundled executable and pack it up with platypus. check theprevent closing option and add run.sh.
import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time


__version__ = "1.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

address = "localhost"


def exe_dir():
    """Return the executable directory."""
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
    elif __file__:
        exe_path = os.path.dirname(__file__)
    return exe_path

server_alive = False
def start_localhost():
    global port
    port = 7999
    while True:
        try:
            port +=1
            print(" - " + address +":" +str(port))
            httpd = socketserver.TCPServer((address, port), http.server.SimpleHTTPRequestHandler)
            print("Web server alive")
            global server_alive
            server_alive = True
            httpd.serve_forever()
            break
        except:
            continue

def open_default_localhost():
    webbrowser.open(url=f"http://localhost:{str(port)}", new=1, autoraise=True)    

def main():
    os.chdir(exe_dir()) # Changes the directory to the executable
    #os.chdir("../../../") # Uncomment for building macOS apps.
    t1 = threading.Thread(target=start_localhost)
    t2 = threading.Thread(target=open_default_localhost)
    t1.start()
    while not server_alive:
        time.sleep(1)
    t2.start()

if __name__ == '__main__':
    main()