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
		