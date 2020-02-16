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
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import threading

__version__ = "0.4"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

PORT = 8000

def open_chrome_localhost():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get("localhost:"+str(PORT))

def start_server():
    global server
    server = socketserver.TCPServer(("localhost", PORT), http.server.SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except OSError:
        server.server_close()
        server.shutdown()
        server.serve_forever()

def stop_server():
    #_exit_prompt = input("To finish, press [Enter]")
    #if _exit_prompt:
    server.server_close()
    server.shutdown()
    exit(0)

def main():
    t1 = threading.Thread(target=start_server)
    t1.start()
    open_chrome_localhost()

main()