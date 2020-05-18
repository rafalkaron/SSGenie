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
import time

__version__ = "1.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

server_up = False

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
            print(f"localhost:{port} is up")
            global server_up
            server_up = True
            httpd.serve_forever()
            break
        except:
            continue        

def main():
    os.chdir(exe_dir()) # Changes the directory to the executable directory.
    # os.chdir("../../../") # Uncomment for building macOS apps.
    threading.Thread(target=start_web_server).start()
    while not server_up:
        time.sleep(1)
    webbrowser.open(url=f"http://localhost:{str(port)}", new=1, autoraise=True)

if __name__ == '__main__':
    main()