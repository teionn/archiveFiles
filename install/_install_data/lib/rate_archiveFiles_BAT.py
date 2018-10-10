# -*- coding: utf-8 -*-
#コーディング: utf-8
#------------------------------------------------------------------------------
import sys

import rate_archiveFiles
#------------------------------------------------------------------------------

def bat2py_path():
    return (sys.argv[1]).split(";")[0]

def bat2py_modeStr():
    return (sys.argv[1]).split(";")[1]

def bat2py_modeDeco():
    return (sys.argv[1]).split(";")[2]

def archiveBAT():
    print rate_archiveFiles.saveMain(bat2py_path(),bat2py_modeStr(),bat2py_modeDeco())
	
	
print "Copying files. Please wait a moment ..."
archiveBAT()
