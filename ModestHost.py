#coding: utf-8
"""
    ModestHost (Codename: SSGenie)
    *********************************************************

    Quickly host files from the ModestHost directory.

    *********************************************************
"""

import http.server
import socketserver
import os
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import threading

__version__ = "0.5"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

address = "localhost"

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

def server():
    httpd = socketserver.TCPServer((address, PORT), http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()

def start_server():
    global PORT
    PORT = 8000
    print("\n>>> Hosting files from " + application_path + " on " + address + ":" + str(PORT)+"\n")
    while True:
        try:
            server()
        except:
            PORT += 1
            server()
        finally:
            continue
        break

def open_chrome_localhost():
    print(">>> Opening a default Google Chrome instance on "+ address + ":" + str(PORT))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(address +":"+str(PORT))

def main():
    os.chdir(application_path)
    t1 = threading.Thread(target=start_server)
    t1.start()
    open_chrome_localhost()
main()