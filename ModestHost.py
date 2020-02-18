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

def enter_dir():
    global host_dir
    try:
        host_dir = input("Enter the full path to the directory that you want to host: ")
        os.chdir(host_dir)
    except:
        print("Try again!") #add an example for each system
        enter_dir()

def current_dir():
    global host_dir
    host_dir = os.getcwd()
    os.chdir(host_dir)

def start_server():
    global PORT
    PORT = 8000
    global address
    address = "localhost"
    print("\n>>> Hosting files from " + host_dir + " on " + address + ":" + str(PORT)+"\n")
    while True:
        try:
            httpd = socketserver.TCPServer((address, PORT), http.server.SimpleHTTPRequestHandler)
            httpd.serve_forever()
        except:
            PORT += 1
            httpd = socketserver.TCPServer((address, PORT), http.server.SimpleHTTPRequestHandler)
            httpd.serve_forever()
   


def open_chrome_localhost():
    print(">>> Opening a default Google Chrome instance on "+ address + ":" + str(PORT))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(address +":"+str(PORT))

def main():
    if os.name=="posix":
        enter_dir()
    if os.name=="nt":
        current_dir()
    t1 = threading.Thread(target=start_server)
    t1.start()
    open_chrome_localhost()

main()