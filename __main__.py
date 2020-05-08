#coding: utf-8
"""
Quickly host files from the ModestHost directory on a localhost web server.
"""
# Compile by using pyinstaller with the --onedir argument. Then, add the files from the compiled directory to the Platypus bundle and use the run.sh file as the Platypus script.
import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

__version__ = "1.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

server_alive = False

def exe_dir():
    """Return the script or executable directory."""
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
    elif __file__:
        exe_path = os.path.dirname(__file__)
    return exe_path

def start_web_server():
    global port
    port = 7999
    while True:
        try:
            port +=1
            httpd = socketserver.TCPServer(("localhost", port), http.server.SimpleHTTPRequestHandler)
            print(f"localhost:{port} is up")
            global server_alive
            server_alive = True
            httpd.serve_forever()
            break
        except:
            continue        

def main():
    os.chdir(exe_dir()) # Changes the directory to the executable
    os.chdir("../../../") # Uncomment for building macOS apps.
    threading.Thread(target=start_web_server).start()
    while not server_alive:
        time.sleep(1)
    webbrowser.open(url=f"http://localhost:{str(port)}", new=1, autoraise=True)

if __name__ == '__main__':
    main()