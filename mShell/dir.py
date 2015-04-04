#!/bin/python
"""

Functions to change directory
To manipulate paths, see the os.path module

"""

import sys
import os

def change(directory):
	print("Currently inside: ", os.getcwd())
	try:
		os.chdir(os.path.join(os.getenv('userprofile'),directory))
	except SystemError:
		print SystemError
	finally:
		print os.getcwd()
		print os.listdir(os.getcwd())
		
#returns a list of files 
def listCurrDir(directr):
		files = os.listdir(os.getcwd())
		return files
#can be used to make a table by doing op("table1").appendRow(file)