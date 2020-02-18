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
address = "localhost"

host_dir = os.path.join(os.path.dirname(__file__))
os.chdir(host_dir)

def start_server():
    print("\n>>> Hosting files from " + host_dir + " on " + address + ":" + str(PORT)+"\n")
    httpd = socketserver.TCPServer((address, PORT), http.server.SimpleHTTPRequestHandler)
    httpd.allow_reuse_address=True
    httpd.serve_forever()

def open_chrome_localhost():
    print(">>> Opening a default Google Chrome instance on "+ address + ":" + str(PORT))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(address + ":"+str(PORT))

def main():
    t1 = threading.Thread(target=start_server)
    t1.start()
    open_chrome_localhost()

main()