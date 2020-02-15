#coding: utf-8
"""
    SSGenie (Static Site Genie)
    ******************************************************

    Quickly host files locally.

    ******************************************************
"""

import http.server
import socketserver
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#import webbrowser
from multiprocessing import Process

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"



def open_chrome_localhost():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get("localhost:8000")
    #webbrowser.register("chrome", None,webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
    #webbrowser.get("chrome").open_new("localhost:8000")

def start_server():
    PORT = 8000
    _script_filepath = os.path.abspath(__file__)
    _script_filename = os.path.basename(__file__)
    _script_directory = _script_filepath.replace(_script_filename, "").replace("\\", "/")
    open_chrome_localhost()
    socketserver.TCPServer(("localhost", PORT), http.server.SimpleHTTPRequestHandler).serve_forever()
    print("Serving files from " + _script_directory + " at localhost:" + str(PORT))

def stop_server():
    _exit_prompt = input("To finish, press [Enter]")
    if _exit_prompt:
        exit(0)

if __name__ == '__main__':
    procs = []
    procs.append(Process(target=open_chrome_localhost, args=('bob',)))
    procs.append(Process(target=start_server, args=('sir',)))
    map(lambda x: x.start(), procs)

start_server()