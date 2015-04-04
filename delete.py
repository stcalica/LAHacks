#!/usr/bin/python
"""

Function to delete

"""

import os, sys
import shutil

def toDelete(toDelete):

    #does not work, how to type cast it so user doesn't have 
    #to type toDelete("test"); want toDelete(test)

    #toDelete = str(toDelete)

    #removes directory and its content
    if (os.path.isdir(toDelete)):
        shutil.rmtree(toDelete)
    elif (os.path.isfile(toDelete)):
        os.remove(toDelete)
    else:
        print("could not file or directory")

"""

#deletes files
def delete():
    print("Delete what")
    toDelete = raw_input(">")
    os.remove(toDelete)

#delete directories, doesn't check if empty
def deleteDirectory():
    print("Which Directory?")
    toDelete = raw_input(">")
    shutil.rmtree(toDelete)

"""