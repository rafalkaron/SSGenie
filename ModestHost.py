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
    global bundle_dir
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

print( 'bundle dir is', bundle_dir )
print( 'sys.argv[0] is', sys.argv[0] )
print( 'sys.executable is', sys.executable )
print( 'os.getcwd is', os.getcwd() )

def current_dir():
    global host_dir
    host_dir = os.getcwd()
    os.chdir(host_dir)

def enter_dir():
    global host_dir
    try:
        host_dir = input("Enter the full path to the directory that you want to host: ")
        os.chdir(host_dir)
    except:
        print("Try again!") #add an example for each system
        enter_dir()



def server():
    httpd = socketserver.TCPServer((address, PORT), http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()

def start_server():
    global PORT
    PORT = 8000
    #print("\n>>> Hosting files from " + host_dir + " on " + address + ":" + str(PORT)+"\n")
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
    if os.name=="nt":
        current_dir()
    if os.name=="posix":
        os.chdir(bundle_dir)

    t1 = threading.Thread(target=start_server)
    t1.start()
    open_chrome_localhost()

main()