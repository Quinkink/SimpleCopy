"""Created on 17 Mar 2020

@author: Eleonore
"""

from os import path
import sys
import urllib.request
import urllib.error
import urllib.parse

def find_data_file(filename, directory=""):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = path.dirname(sys.executable) + '\\' + directory
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        if directory == "":
            datadir = ""
        else:
            datadir = directory + '/'
            # datadir = path.dirname(__file__) + '/../' + directory + '/'
    
    return path.join(datadir, filename)
