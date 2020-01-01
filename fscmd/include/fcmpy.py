"""
 (C) Copyright 2019 Faran, All Rights Reserved
 Fcmpy (Fcm to Py with _parse_to_reading function)
"""

import os, sys, py2exe #basic
from distutils.core import setup #to compile

firstSentence="""'''
 (C) 2019 Faran, All Rights Reserved
  This is FCM Script compiled to Python Script
 Version = 0.1
'''

import os, sys #basic requirement
try:
    import lexer #try import from the module folder
except:
    from include import lexer #try import from fscmd module

#create main() function
def main(_arg=None):
"""
lastSentence="""
if __name__ == "__main__":
    main()"""

def Compile(nort):
    ret = ''
    for s in nort.split('\n'):
        ret += '\tlexer._parse_to_reading("'+s+'")\n'
    return ret
    
def Complete(source):
    return firstSentence+Compile(source)+lastSentence
    
def Creating(source, filename='main.py'):
    try:
        open(filename, 'w').write(Complete(source))
    except:
        pass
    
def CSetup(filename):
    open('setup.py', 'w').write("""from cx_Freeze import setup, Executable
setup(executables = [Executable('"""+filename+"""')])""")

def toExe(source, filename='main.py', rewrite=True):
    if rewrite:
        CSetup(filename)
    Creating(source, filename)
    os.system('py setup.py build')