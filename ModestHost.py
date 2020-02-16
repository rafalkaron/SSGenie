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

def start_server():
    httpd = socketserver.TCPServer(("localhost", PORT), http.server.SimpleHTTPRequestHandler)
    httpd.allow_reuse_address=True
    httpd.serve_forever()

def open_chrome_localhost():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get("localhost:"+str(PORT))

def main():
    t1 = threading.Thread(target=start_server)
    t1.start()
    open_chrome_localhost() 

main()