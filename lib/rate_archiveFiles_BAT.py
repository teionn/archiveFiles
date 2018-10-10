# -*- coding: utf-8 -*-
#コーディング: utf-8
#------------------------------------------------------------------------------
import sys

import rate_archiveFiles
#------------------------------------------------------------------------------

def bat2py_join():
	getPath=unicode(sys.argv[1].replace("~"," "),'cp932')  
	return getPath

def bat2py_path():
    return bat2py_join().split(";")[0]

def bat2py_modeStr():
    return bat2py_join().split(";")[1]

def bat2py_modeDeco():
    return bat2py_join().split(";")[2]

def archiveBAT():
    print rate_archiveFiles.saveMain(bat2py_path(),bat2py_modeStr(),bat2py_modeDeco())
	
	
print "Copying files. Please wait a moment ..."
archiveBAT()
