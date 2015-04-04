#!/bin/python
"""

Functions to mess with processes
uses the subprocess library
"""

import sys, os
import psutil, subprocess

def start_process(process):
	subprocess.Popen(process) #allows you to run and keep the shell open 
	
def stop_process(process):
	for proc in psutil.process_iter():
		if proc.name() == PROCNAME:
			proc.kill()

def back_process(process):
	pass
	
def list_processes(process):
	pass

