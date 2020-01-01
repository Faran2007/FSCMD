import signal, sys, os, random, re, time, importlib, colorama, subprocess # basic import for .exe system

try:
 sys.path.extend([os.path.abspath(""), os.path.abspath("include")])
except:
 pass

try:
 from include import lexer
except:
 try:
  import lexer
 except ImportError as ie:
  print("FSCMD:: lexer.py is the heart of fscmd, and not exist. This is a real FATAL ERROR. Please download FSCMD again")
  sys.exit()

""" 
 (C) Copyright 2019-2020 Muhammad Faran Aiki, All Rights Reserved
 
 FSCMD REAL FILE,
  READ README.TXT
 
 Environment for FSCMD
 
 I'm sure that you download this file using RAW Method aren't ya?
 
 Lexer of fscmd with _raw_ setting
  This is the almost-heart of fscmd
  
 Please DO NOT Edit this if you don't know how to do it 
  
 Please DO NOT COPY THIS Except if you have the permission and right
  to copy, permission only be given from Faran (Owner)
  
 Read "readme.txt" and "help.txt" for more information
"""

"""
 Initialization
"""
colorama.init(autoreset=True)

""" Handler """
try:
 lexer._parse_to_reading
except NameError:
 print("FSCMD:: _parse_to_reading is not storaged in lexer.py [FATAL]")
 sys.exit()
  
"""
 Database for current file
"""
isExit = False

"""
 File argument!
"""
#here it is
try:
 if len(sys.argv) > 1:
  if sys.argv[1].strip().lower() in ('-h', '--help'):
   print("""Helper for argument vector fscmd
 '-h' or '--help' to show this
 '-ver' or '--version' to show version
 '-sys' or '--system' to show system format for fscmd
 '-dev' or '--developer' to show developer of current fscmd
 '-e' or '--execute' or '--exec' to execute a single line of command
 '-lic' or '--license' to show license information
""", end='')
   isExit = True
  elif sys.argv[1].strip().lower() in ('-lic', '--license'):
   print('(C) Copyright 2019-2020 Muhammad Faran Aiki, All Rights Reserved.')
   isExit = True
  elif sys.argv[1].strip().lower() in ('-e', '--execute', '--exec'):
   try:
    lexer._parse_to_reading(' '.join(sys.argv[2::]).strip())
   except Exception as e:
    print(e)
   isExit = True
  elif sys.argv[1].strip().lower() in ('-dev', '--developer'):
   try:
    print(lexer.__developer__)
   except:
    pass
   lexer.DataGlobal['ret'] = lexer.__developer__
   isExit = True
  elif sys.argv[1].strip().lower() in ('-ver', '--version'):
   try:
    print(lexer.__version__)
   except:
    pass
   lexer.DataGlobal['ret'] = lexer.__version__
   isExit = True
  elif sys.argv[1].strip().lower() in ('-sys', '--system'):
   try:
    print(lexer.__system__)
   except:
    pass
   lexer.DataGlobal['ret'] = lexer.__system__
   isExit = True
  elif sys.argv[1].strip().lower() in ('-m', '--module'):
   if len(sys.argv) > 2:
    try:
     try:
      open(lexer.loadpath+sys.argv[2]+'.fcm')
     except:
      open(lexer.loadpath+sys.argv[2])
     print('Module "'+sys.argv[2]+'" is exist')
    except:
     print('Module "'+sys.argv[2]+'" is not exist')
   else:
    lexer._shower_module()
    isExit = True
   isExit = True
  else:
   try:
    lexer.modulefile = sys.argv[1]
    lexer.moduleline = 1
    lexer.DataGlobal['_filename'] = lexer.modulefile
    lexer.executefile(sys.argv[1])
    lexer.docstring[sys.argv[1]] = lexer.allComment
    signal.signal(signal.SIGINT, lexer.signal_handler_file)
    isExit = True
   except FileNotFoundError:
    print('From fscmd.py, file is not exist "'+sys.argv[1]+'"')
    isExit = True
 else:
  print('''(C) Copyright 2019-2020 Muhammad Faran Aiki, All Rights Reserved.
@FSCMD. Everyone can be a programmer, distributor or a creator, by typing \'?\'.'
You are using "'''+lexer.__developer__+'''" distribute at version "'''+str(lexer.__version__)+'''" and using System "'''+str(lexer.__system__)+'''" and still in development.''')
  lexer._parse_to_reading('console_status := "active"\nsetCommandAsFunction console_status', ReplaceNewLine=False)
except NameError as e:
 if "lexer.__dev__" in str(e):
  print('FSCMD:: __dev__, __type__, and __system__ is not storaged in lexer.py.')
 else:
  print("PythonError:: "+str(e))
 sys.exit()
except Exception as e:
  print("PythonError:: "+str(e))
  
#On Console  
if __name__ == '__main__' and not isExit:
 signal.signal(signal.SIGINT, lexer.signal_handler)
 while True:
  sys.stdout = sys.__stdout__
  sys.stdin  = sys.__stdin__
  try:
   if not lexer.local_num and not lexer.in_comment:
    put_ = input(lexer._cursor)
   elif lexer.in_comment:
    put_ = input(lexer._comt_cursor)
   else:
    put_ = input(lexer._loc_cursor)
   sys.stdout = lexer.last_stdout
   sys.stdin = lexer.last_stdin
   lexer._parse_to_reading(put_, ReplaceNewLine=False)
   lexer.history_com.append(put_)
   lexer.last_stdout = sys.stdout
   lexer.last_stdin  = sys.stdin
  except EOFError:
   pass
  except SystemExit:
   sys.exit()
  if lexer.DataGlobal['ret'] == '':
   print(lexer.DataGlobal['ret'], end='')
  elif not lexer.local_num:
   print(lexer.DataGlobal['ret'])
  lexer.DataGlobal['ret'] = ''