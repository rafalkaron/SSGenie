#coding: utf-8
"""
    ModestHost (Codename: GT)
    *********************************************************

    Stop ModestHost.

    *********************************************************
"""
import os

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

os.popen("pkill -9 -f ModestHost.py")
exit(0)