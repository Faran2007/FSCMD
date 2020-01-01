"""
 (C) Copyright 2019-2020 Muhammad Faran Aiki, All Rights Reserved.
 
 Important module,
  remove this cause permanent damage
  
 This module is used against `pydef`, `def`, `void`, and `pyvoid`
  and of course the absolute operator
 
 This is manipulator for 
  string, list, set .etc to 
  lexer.py 
  
 Please do not edit this if you don't know how to use it
  If you want to use it in lexer.py, be sure to use "Manipulator.${command}" because
  this module is imported with it's name
"""

# def 
def stringifydef(string, method=None):
 if method is None:
  method = lambda x:x
 return method(string.replace('\\\\n', '\\n').replace('\\', '\\\\').replace('"', '\\"').replace('\'', '\\\''))

#pydef
def stringifypydef(string, method=None): 
 if method is None:
  method = lambda x:x 
 return method(string.replace('\\"', '\\\\"').replace("\\'", "\\\\'").replace("\"", '\\"').replace('\'', '\\\''))
 
def lcalstring(string, method=None):
 if method is None:
  method = lambda x:x 
 return method(string.replace('\\', '\\\\').replace('"', '\\"').replace('\'', '\\\''))
 
def ReverseDict(Dict):
 try:
  return dict(zip(list(Dict.values()), list(Dict.keys())))
 except:
  return dict(zip([tuple(val) for val in Dict.values()], Dict.keys()))