import os, sys, importlib, time, random, re, signal, subprocess #basic py.import for system module
try:
 import Manipulator
except:
 from include import Manipulator
"""
 Lexer.__type__ = 0.1, Dev = Faran, 1, Script: Internal/Built, Open-Source: True
 Original: True, Editable = True, Masterpiece = Well Yes

 (C) Copyright 2019-2020 Muhammad Faran Aiki, All Rights Reserved

 We achieve what we dream, we accomplish what we want       | Please help me
 We compress our method, we simplify the problem            |   We need this
 We solve many error, we handle many exception              |       To success
 We improve many, we enchant so goodly                      |   Debug this project
 
 Created using `Python` and some `FSCMD`, `Python` by Guido Van Rossum, `FSCMD` by Faran
 
 All of this script is mine but you can use it properly / create a new script using this file BUT please credit me for the basic programming language
  The script was actually made for easy-programming-developing.
  Please note, for Real Programmer. Please use this program wisely and do not hack this
  program because this programming language was created by 12 years old (I'm serious) and will have a birthday at 8th April 2020
  
 First programming language that use free-form style and fancy style 
  
 You can create your own script and named it lexer.py to replace this file but don't
  remove all of it because, yeah... you will know what's the problem here
  
 ** 
  PLEASE NOTE THAT
   if you want to use `_parse_to_reading` for a scoped command 
   (for example: _parse_to_reading(DataRestrict['local'])), please use `ReplaceNewLine=False`
   to instruct lexer to not replacing any newline
 **
 
 Please help me solve bugs, because I know we need someone to become someone
 
 This is my project and open source, please DO NOT STEAL IT
 But please distribute it and then you can edit it but still credit me :D
 
 Created by Muhammad Faran Aiki at Home in Depok
 
 _parse_to_reading -> main function 
 _reading          -> parse the given argument from _parse_to_reading
 
 Still in Improvisation
"""

"""
 File data
"""
__version__     = 0.1
__system__      = 1.5
__isoriginal__  = True
__developer__   = 'Muhammad Faran Aiki'

"""
 Basic Data
  Basic Data are often used to create something 
  
 Basic Data actually was a global data
  Basic. Script. Exe.
  
 Global and Internal are used in this programming method
 
 REAL Data, COMMAND Data, SPECIAL COMMAND Data
  are defined here and you can edit it
 
 You can edit the lexer standard data [lestda] here..
"""
docstring       = {'builtin': 'First module to get executed', '$Console': 'Console system (CLI)'}
modulefile      = '$Console'
moduleline      = 1
fileScript      = []
AllScoped       = ['local', 'void', 'pyvoid', 'for', 'while', 'if', 'scope', 'pyscope', 'try', 'catch'] # all scoped a.k.a. special scope a.k.a. in-file scope
AllAScope       = ['void', 'for', 'while', 'if', 'scope', 'try', 'catch'] # all available scoped command that interact with parent scoped (for example 'for' will add local_num statement)
AllObject       = {}
AllCommand      = {'builtin/standard command (lexer.py)': [], '$Console': []}  
AllClass        = {'builtin/standard class (lexer.py)': []}
AllCScope       = {}
AllPScope       = {}
asFunction      = []
DataGlobal      = {'ret': '', '_spacebar': ' ', '_dollar': '$', '_sharp': '#', '_percent': '%', '_newline': '\\\\n', '_arg': '', '_commasplit': '', '_splitarg': '', '_argv': sys.argv[2::], '_argc': len(sys.argv[2::]), '_argvs': ' '.join(sys.argv[2::]), '_argvc': ' '.join(sys.argv[2::]).split(',')}
DataRestrict    = {'local': ''}
SectionLabel    = {'end': 0, 'start': 0}
eFirstOperator  = set()
FirstOperator   = {'*': '', '//': 'pass', '"': '', '\'': '', "-": '', ';': 'run', '?': 'help'}
SecOperator     = {}
eLastOperator   = set()
fLastOperator   = set()
LastOperator    = {'++': '', '--': ''}
AbsOperator     = {}
local_num       = 0
csp_com         = "" 
arrow_data      = []
arrow_type      = ''
in_comment      = False
_cursor         = '<:> ' # _cursor basic
_loc_cursor     = '::: ' # _at local cursor
_comt_cursor    = '### ' # _at comment cursor
_std_cursor     = '$-\\'+os.path.abspath('').replace('\\', '\\')+'>> '
allException    = []
allComment      = ''
last_local      = ''
_handler_exc    = '' # handler to execution
exc_hide        = False
_try_exc        = False # check exception if true
redir_catch     = []
each_com        = ''
local_type      = ''
l_local_type    = ''
scope_data      = {}
l_scope_data    = {}
this_rcmd       = ''
last_rcmd       = ''
scope_line      = 0
isAutoRepln     = True  # check if this module is imported by python
last_stdout     = sys.__stdout__
last_stdin      = sys.__stdin__
history_com     = []
debug_com       = ''

"""
 Important variable, or almost never used for
  normal code (but useful for big code)
"""
maxint       = sys.maxsize
maxunicode   = sys.maxunicode
maxfloat     = 15
TrueList = ['true', 'yes', 'live', 'on', 'itis', 'it\'s', 'yeah', 'yep', 'right', '1', 'benar', 1, True]
FalseList = ['false', 'no', 'dead', 'off', 'itisnt', 'it\'snt','nah', 'nope', 'left', 'wrong', '0', 'salah', 0, False]

"""
 Basic System Requirement
  for object/data 
  
 Defined here..
"""
if sys.argv[0].endswith('fscmd.py') or sys.argv[0].endswith('fscmd.exe'):
 filepath = os.path.abspath('')+'\\'
elif sys.argv[0].endswith('lexer.py') or sys.argv[0].endswith('lexer.exe'):
 filepath = sys.argv[0].split('lexer.py', 1)[0].split('lexer.exe', 1)[0].strip().strip('\\').split('include', 1)[0].strip('\\')+'\\'
else:
 filepath = os.path.abspath('')
folderpath   = filepath.split('fscmd.py', 1)[0].split('fscmd.exe', 1)[0].strip().strip('\\')+'\\'
loadpath     = folderpath+'\\module\\'
includepath  = folderpath+'\\include\\'
otherpath    = folderpath+'\\other\\'

""" Preparation """
sys.path.extend([loadpath, includepath, filepath])
sys.setrecursionlimit(maxint)

try:
 import DataTypes
except ImportError as ie:
 try:
  from include import DataTypes 
 except:
  print('FSCMD:: Included module is not found! "DataTypes.py" OR such a class doesn\'t exist in DataTypes.py, please fix this or reinstall FSCMD')
  sys.exit()

modulefilebefore = DataTypes.null()

""" External data link"""
try:
 AllHelper = eval(open(folderpath+'include/DescriptionHelper.json').read())
except:
 try:
  AllHelper = eval(open(folderpath+'DescriptionHelper.json').read())
 except Exception as e:
  AllHelper = {}
  print('Description is not available, this will make the builtin command doesn\'t have helper')

"""
 Classed function for more
  external and internal function
  
 Exception: Based Exception
 Lexer:     Based Lexer
 _Arg :     Based Argument
"""
def signal_handler(signal, type):
 try:
  print('')
 except SystemExit:
  sys.exit()
  
def signal_handler_file(signal, type):
 sys.exit()

def catch(rcmd):
 global _try_exc, allException
 bAllException = allException
 allException = []
 _try_exc = True
 _parse_to_reading(rcmd)
 _try_exc = False
 if len(allException) == 0:
  allException = bAllException
  return True #success
 allException = bAllException
 return False #failed

def executefile(filepath, isNamedAsModule=False):
 global modulefile, moduleline, SectionLabel, DataRestrict, history_com, debug_com
 try:
  prevfile = modulefile
  prevline = moduleline
  prevsect = SectionLabel
  prevrest = DataRestrict
 except:
  pass
 signal.signal(signal.SIGINT, signal_handler_file)
 fileScript = open(filepath, 'r', encoding='utf-8').read().split('\n')
 r = len(fileScript)
 if isNamedAsModule:
  modulefile = filepath.split('\\')[-1].strip()
 else:
  modulefile = filepath
 moduleline = 1
 DataGlobal['_filename'] = modulefile
 SectionLabel['end'] = r+1
 while moduleline < r+1:
  _parse_to_reading(fileScript[moduleline-1], ReplaceNewLine=False)
  history_com.append(fileScript[moduleline-1])
  moduleline += 1
 try:
  modulefile   = prevfile
  moduleline   = prevline
  SectionLabel = prevsect
  DataRestrict = prevrest
 except Exception as e:
  pass
 if modulefile == '$Console':
  signal.signal(signal.SIGINT, signal_handler)

def _create_shower_help(firstText, elemDict, eachRow=7, isDual=False):
 char = 0
 print(firstText, end='\n  ')
 if len(elemDict) != 0:
  for _o in elemDict:
   char += 1
   if char == eachRow:
    end_ = '\n  '
    char = 0
   else:
    end_ = ' '
   if isDual:
    print('(%s, %s)' % elemDict[_o], end=end_)
   else:
    print(_o, end=end_)
  print('')
 else:
  print('None')

def _shower_module(location=loadpath):
 char = 0
 modl = sorted([a.replace('.fcm', '') for a in os.listdir(loadpath) if a.endswith('.fcm') and os.path.isfile(location+a)])
 print('All module available in standard folder:', end='\n  ')
 if len(modl) != 0:
  for _o in modl:
   char += 1
   if char == 7:
    end_ = '\n  '
    char = 0
   else:
    end_ = ' '
   print(_o, end=end_)
  print('')
 else:
  print('None')
 
def _shower_help_special(type):
 type = type.strip().lower()
 if type == 'faran':
  print("""Faran is the owner and the founder of FSCMD from 2019 in Indonesia as a 12 years old person.
Faran live in Indonesia, West Java -> Depok and study in SMPN 3 Depok.
Faran's full name is `Muhammad Faran Aiki`.
Faran's age is 12 years old and will continue to 13 years old when 8th April 2020 comes out. 
Faran's full (almost) biodata can be found at 'https://www.muhammadfaranaiki.blogspot.com'
Faran's having fun and hard time because of this project :D
Faran's now at his home for holidays
Faran love philosophy, math, eat, drink, science, social and logic
Faran didn't solve all problem in this project because you are the one who will solve it :D (I will feature you)
Faran can't be called dumb (idiot) or smart (jenius) yet :D
Faran build FSCMD project and the deadline is at 1 January 2020
Faran went 1/2 years (not full because I HAVE A SCHOOL) to create this project""")
 elif type == 'fscmd':
  print('"FSCMD" is the son of "Python" and grandson of "C", a familiar language that will make you familiar again :D')
 elif type == 'help':
  print('Type "?" for more help')
 elif type.strip().lower() in [_a.lower().rsplit('.', 1)[0].strip() for _a in os.listdir(otherpath)]:
  try:
   print(open(otherpath+''.join(_file for _file in os.listdir(otherpath) if _file.lower().startswith(type))).read())
  except:
   pass
 elif type == 'operator':
  print("""Operator is divided to 4 section (see "?procedure") and 3 special section (see "?procedure"), type
 "?firstoperator" for first operator (Contain 1 Special)
 "?secoperator" for second operator
 "?lastoperator" for last operator
 "?absoluteoperator" for absolute operators
You can add operator using command below
 "addFirstOperator" for first operator
 "addFirstOperatorEscape" for first escape operator
 "addSecondOperator" for second operator
 "addLastOperator" for last operator
 "addLastOperatorForce" for last force operator
 "addLastOperatorEscape" for last escape operator
 "addAbsoluteOperator" for absolute operator
You can remove operator using command below
 "removeFirstOperator" for first operator
 "removeFirstOperatorEscape" for first escape operator
 "removeSecondOperator" for second operator
 "removeLastOperator" for last operator
 "removeLastOperatorForce" for last force operator
 "removeLastOperatorEscape" for last escape operator
 "removeAbsoluteOperator" for absolute operator
""", end='')
 elif type in ['firstoperator', 'FirstOperator', 'oneoperator']:
  _create_shower_help("""First operator is operator that execute if the operator is in the first index of command
You can get the helper of the operator by using "?{operator}", for example "?:"
 
However, this operator has a special case, that's first operator escape
This operator will operate IF only the first index of space doesn't contain any command and this operator won't execute if there's a second operator

Here is the defined first operator:""", FirstOperator, 14)
 elif type in ['secoperator', 'secondoperator', 'midoperator']:
  _create_shower_help("""Second operator is operator that execute if the operator is in the middle of the command
You can get the helper of the operator by using "?{operator}", for example "?+"

Here is the defined second operator:""", SecOperator, 14)
 elif type in ['lastoperator', 'thirdoperator', 'lstoperator']:
  _create_shower_help("""Last operator is operator that execute if the operator is in the last of the command
You can get the helper of the operator by using "?{operator}", for example "?++"

However, this operator has a special case, that's last operator force and last operator escape
This operator will always operate if the operator is in the last of the command line no matter what there's command, second operator, first operator or not (Force)
This operator will operate if the operator is in the last of the command line and if there's no command or second operator                                  (Escape)

Here is the defined last operator""", LastOperator, 14)
 elif type in ['absoluteoperator', 'absoperator', 'dualoperator']:
  _create_shower_help("""Absolute operator a.k.a Dual operator is operator that will operate if command line start with operator1 and end with operator2
You can get the helper of the operator by using "?{operator}", for example "?[ ]"
  
Here is the defined absolute operator""", AbsOperator, 14, isDual=True)
 else:
  raise 
  
def _shower_command():
 for comtypes in AllCommand:
  char = 0
  print(comtypes+':', end='\n')
  for com in sorted(AllCommand[comtypes]):
   char += 1
   if char == 7:
    end_ ='\n'
    char = 0
   else:
    end_ =''
   print('  '+com, end=end_)
  print('\n')

def _shower_class():
 for clastypes in AllClass:
  char = 0
  print(clastypes+':', end='\n')
  for clas in sorted(AllClass[clastypes]):
   char += 1
   if char == 7:
    end_ ='\n'
    char = 0
   else:
    end_ =''
   print('  '+clas, end=end_)
  print('\n')

def _shower_some_command(comtypes):
 char = 0
 try:
  AllCommand[comtypes]
  print(comtypes+':', end='\n')
 except:
  pass
 for com in sorted(AllCommand[comtypes]):
  char += 1
  if char == 7:
   end_ ='\n'
   char = 0
  else:
   end_ =''
  print('  '+com, end=end_)
 print('\n')

def _parse_to_reading(compiled, isLocalNumUsed=True, isCommentUsed=True, ReplaceNewLine=True):
 global local_num, this_rcmd, last_rcmd, local_type, allComment
 """
  This is the start of the command, where almost every code
   to parse use `_parse_to_reading`
 """
 if ReplaceNewLine:
  compiled = compiled.replace('\n', '\\n')
 if compiled.strip() != "":
  for ec in compiled.split('\n'):
   if isLocalNumUsed:
    _parse_before_reading(ec, isCommentUsed)
   else:
    _reading(ec)
 elif in_comment:
  allComment += '\n'
 return DataGlobal['ret']
    
def _parse_before_reading(ec, icu=True):
 """
  check last_rcmd, local_num ....
 """
 global local_num, this_rcmd, last_rcmd, local_type, scope_line, allComment
 if not local_num and (not in_comment or not icu) or ec.strip().split(' ', 1)[0].strip().lower() in AllScoped or (ec.strip().lower()+" ").startswith('end ') or ec.strip().startswith('"') and not local_num or ec.strip().startswith("'") and not local_num:
  this_rcmd = ec
  _reading(str(ec).strip())
  last_rcmd = ec
 elif local_num and scope_line > 0:
  scope_line += 1
  DataRestrict['local'] += str(ec).replace('\\n', "\\\\\\n")+'\n'
 elif in_comment:
  allComment += ec+'\n'
    
def _reading(rcmd):
 """
  Convert normal rcmd to converted data rcmd
  Read rcmd as 
   argument, split argument, and comma argument
 """
 global in_comment, DataGlobal, DataRestrict, allComment
 rcmd = rcmd.replace('\\\\n', '\\n')
 all_command = [i for s in AllCommand.values() for i in s]
 if '#' in rcmd:
   if '[' in rcmd and ']' in rcmd: 
    for _li in re.findall('\#\[.*\]', rcmd.replace('#[', '\n#[')):
     rcmd = rcmd.replace(_li, str(_parse_to_reading(_li.strip('#')[1:][:-1])))
   if '(' in rcmd and ')' in rcmd: 
    for _li in re.findall('\#\(.*\)', rcmd.replace('#(', '\n#(')):
     rcmd = rcmd.replace(_li, str(_parse_to_reading(_li.strip('#')[1:][:-1])))
   if '{' in rcmd and '}' in rcmd:
    for _li in re.findall('\#\{.*\}', rcmd):
     rcmd = rcmd.replace(_li, str(_parse_to_reading(_li.strip('#')[1:][:-1])))
 if '$' in rcmd:
  for _c in reversed(list(DataGlobal)):
   if '{' in rcmd and '}' in rcmd and _c in rcmd:
    rcmd = rcmd.replace('${'+_c+'}', str(DataGlobal[_c]).replace('\n', '\\n'))
   if '(' in rcmd and ')' in rcmd and _c in rcmd:
    try:
     rcmd = rcmd.replace('$('+_c+')', str(len(DataGlobal[_c])))
    except:
     rcmd = rcmd.replace('$('+_c+')', str(len(str(DataGlobal[_c]))))
   if '<' in rcmd and '>' in rcmd and _c in rcmd:
    try:
     rcmd = rcmd.replace('$<'+_c+'>', ', '.join([str(a) for a in DataGlobal[_c]]))
    except:
     pass
 try:
  isTypedNum = float(rcmd.replace(' ', '').strip('f'))
  isTypedNum = True
 except:
  isTypedNum = False
 for _n in DataRestrict:
  rcmd = rcmd.replace('%{'+_n+'}', str(DataRestrict[_n]))
 if rcmd.strip() in DataGlobal and not rcmd.strip() in all_command:
  DataGlobal['ret'] = DataGlobal[rcmd.strip()]
  rcmd = ''
 elif isTypedNum:
  if '.' in rcmd or 'f' in rcmd:
   DataGlobal['ret'] = float(rcmd.replace(' ', ''))
  else:
   try:
    DataGlobal['ret'] = int(rcmd.replace(' ', ''))
   except:
    DataGlobal['ret'] = float(rcmd.replace(' ', '').strip('f'))
  rcmd = ''
 elif rcmd.strip().lower() in TrueList:
  DataGlobal['ret'] = True
  rcmd = ''
 elif rcmd.strip().lower() in FalseList:
  DataGlobal['ret'] = False
  rcmd = ''
 elif rcmd.startswith('*'):
  global csp_com
  csp_com = rcmd.strip().split('*', 1)[1].strip()
  rcmd = ''
 elif rcmd.startswith(';'):
  rcmd = 'run ' + rcmd.split(';', 1)[1]
 elif rcmd.startswith('-') and csp_com.strip() != '':
  rcmd = csp_com +' '+ rcmd.strip().split('-', 1)[1]
 elif rcmd.strip().lower() in AllObject:
  DataGlobal['ret'] = AllObject[rcmd.strip().lower()].__return__()
  rcmd = ''
 elif rcmd.strip().endswith(']') and '[' in rcmd.strip() and not rcmd.strip().startswith('[') and not any(' '+a+' ' in rcmd.strip().lower() for a in SecOperator) and not any(a for a in FirstOperator if rcmd.startswith(a)) and not rcmd.strip().lower().split(' ')[0] in all_command:
  try:
   DataGlobal['ret'] = _parse_to_reading(rcmd.split('[')[0].strip())[int(rcmd.split('[')[1].strip().strip(']'))-DataGlobal['base-index']]
  except IndexError:
   exception('index out of the range (max index: "'+str(len(DataGlobal['ret'])+DataGlobal['base-index']-1)+'")')
  except ValueError:
   exception('given argument should be integer')
  finally:
   rcmd = ''
 elif rcmd.strip().endswith(')') and '(' in rcmd.strip() and not rcmd.strip().startswith('(') and not any(' '+a+' ' in rcmd.strip().lower() for a in SecOperator) and not any(a for a in FirstOperator if rcmd.startswith(a)) and not rcmd.strip().lower().split(' ')[0] in all_command:
  try:
   rcmd = rcmd.split('(', 1)[0].strip() + ' ' + str(_parse_to_reading(rcmd.split('(', 1)[1].strip().rsplit(')', 1)[0], ReplaceNewLine=False)).replace('\n', '\\n')
  except Exception as e:
   print(e)
 elif rcmd.strip().endswith('}') and '{' in rcmd.strip() and not rcmd.strip().startswith('{') and not any(' '+a+' ' in rcmd.strip().lower() for a in SecOperator) and not any(a for a in FirstOperator if rcmd.startswith(a)) and not rcmd.strip().lower().split(' ')[0] in all_command:
  try:
   DataGlobal['ret'] = _parse_to_reading(rcmd.split('{')[0].strip())[_parse_to_reading(rcmd.split('{')[1].strip()[:-1])]
  except KeyError:
   exception('Key doesn\'t exist "'+DataGlobal['ret']+'"')
  except TypeError:
   exception('Given data is not a "dict"')
  finally:
   rcmd = ''
 elif rcmd.strip().startswith('?'):
  rcmd = 'help '+rcmd.split('?', 1)[1].strip()
 elif (rcmd.strip().startswith('\'\'\'') or rcmd.strip().startswith('\\\'\\\'\\\'')) and not local_num or (rcmd.strip().startswith('\"\"\"') or rcmd.strip().startswith('\\\"\\\"\\\"')) and not local_num:
  if in_comment:
   allComment = allComment.strip('\n')
   DataGlobal['ret'] = allComment
   in_comment = False
  else:
   allComment = ''
   in_comment = True
  rcmd = ''
 elif rcmd.strip().startswith('//'):
  rcmd = ''
 elif any(a for a in fLastOperator if rcmd.strip().endswith(a)):
  op = ''.join(a for a in fLastOperator if rcmd.strip().endswith(a))
  rcmd = LastOperator[op] + ' ' + rcmd[0:-len(op)]
 elif any(a for a in FirstOperator if rcmd.strip().startswith(a) and a != '-') and not any(a for a in eFirstOperator if rcmd.strip().lower().startswith(a)) and not any([a for a in AbsOperator if rcmd.strip().lower().startswith(a[0]) and rcmd.strip().lower().endswith(a[1])]):
  op = ''.join(a for a in FirstOperator if rcmd.startswith(a))
  rcmd = FirstOperator[op] + ' ' + rcmd[len(op):]
 elif any(a for a in eFirstOperator if rcmd.strip().startswith(a)) and not rcmd.strip().split(' ')[0].lower() in all_command and not any(' '+a+' ' in rcmd.strip().lower() for a in SecOperator) and not any([a for a in AbsOperator if rcmd.strip().lower().startswith(a[0]) and rcmd.strip().lower().endswith(a[1])]):
  op = ''.join(a for a in FirstOperator if rcmd.startswith(a))
  rcmd = FirstOperator[op] + ' ' + rcmd[len(op):]
 elif rcmd.strip().endswith('++') and not rcmd[0:-3].strip() in [i for s in AllCommand.values() for i in s] and not any(' '+a+' ' in rcmd.strip().lower() for a in SecOperator):
  rcmd = 'add ' + rcmd[0:-2].strip() + ', 1'
 elif rcmd.strip().endswith('--') and not rcmd[0:-3].strip() in [i for s in AllCommand.values() for i in s] and not any(' '+a+' ' in rcmd.strip().lower() for a in SecOperator):
  rcmd = 'add ' + rcmd[0:-2].strip() + ', -1'
 elif any(a for a in LastOperator if rcmd.endswith(a)) and not rcmd[0:-(len(''.join(a for a in LastOperator if rcmd.endswith(a))))-1].strip() in [i for s in AllCommand.values() for i in s] and not any(' '+a+' ' in rcmd.strip().lower() for a in SecOperator) and not any(a for a in fLastOperator if rcmd.strip().endswith(a)) and not any(a for a in eLastOperator if rcmd.strip().endswith(a)) and not any([a for a in AbsOperator if rcmd.strip().lower().startswith(a[0]) and rcmd.strip().lower().endswith(a[1])]):
  op = ''.join(a for a in LastOperator if rcmd.endswith(a))
  rcmd = LastOperator[op] + ' ' + rcmd[0:-len(op)]
 elif any(a for a in eLastOperator if rcmd.strip().endswith(a)) and not rcmd.strip().split(' ')[0].lower() in all_command and not any(' '+a+' ' in rcmd.strip().lower() for a in SecOperator) and not any([a for a in AbsOperator if rcmd.strip().lower().startswith(a[0]) and rcmd.strip().lower().endswith(a[1])]):
  op = ''.join(a for a in eLastOperator if rcmd.strip().endswith(a))
  rcmd = LastOperator[op] + ' ' + rcmd[0:-len(op)]
 try:
  if (rcmd.strip().split(' ')[0].strip().lower() not in all_command or rcmd.strip().split(' ')[0].strip().lower() in asFunction) and any(' '+a+' ' in rcmd.strip().lower() for a in SecOperator):
   try:
    l_rcm = rcmd
    subj = ''.join([a+' ' for a in SecOperator if ' '+a+' ' in rcmd.strip().lower()]).strip().split(' ')[0]
    if subj == '=' or subj == '->' or subj == '→':
     op = [i.strip() for i in rcmd.strip().split(' '+subj+' ', 1)]
    else:
     op = [i.strip() for i in rcmd.strip().rsplit(' '+subj+' ', 1)]
    rcmd = (SecOperator[subj] + ' ' + op[0].strip() + ', ' + op[1]).strip()
    if any([a for a in AbsOperator if l_rcm.strip().lower().startswith(a[0]) and l_rcm.strip().lower().endswith(a[1])]):
     try:
      if not catch(rcmd):
       rcmd = l_rcm
     except:
      rcmd = l_rcm
   except:
    pass
 except Exception as e:
  print(e)
 if any([a for a in AbsOperator if rcmd.strip().lower().startswith(a[0]) and rcmd.strip().lower().endswith(a[1])]):
  op = [a for a in AbsOperator if rcmd.strip().lower().startswith(a[0]) and rcmd.strip().lower().endswith(a[1])][0]
  rcmd = AbsOperator[op] + ' ' + rcmd.strip()[len(op[0]):][:-len(op[1])]
 rcmd = rcmd.replace('\\', '\\\\').replace('\\\\n', '\\n').replace('\'', '\\\'').replace('"', '\\"')
 cmd = rcmd.strip().lower().split(' ', 1)[0]
 try:
  co = rcmd.strip().split(' ', 1)[1]
  splitr = co.split(' ')
  splitc = co.split(',')
 except:
  co = ''
  splitr = []
  splitc = []
 splitc = [_c.strip().replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\') for _c in splitc]
 splitr = [_c.strip().replace("\\'", "'").replace('\\"', '"').replace('\\\\', '\\') for _c in splitr]
 if rcmd.strip() == '':
  cmd = 'pass'
 lexer(str(cmd), str(co), str(splitr), str(splitc))

def scope_creator(name, _arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_line
  if local_num:
   DataRestrict['local'] += this_rcmd + '\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   DataRestrict['local'] = ''
   if local_type == "":
    local_type = name
   scope_line += 1
   local_num += 1
   scope_data['_arg'], scope_data['_commasplit'], scope_data['_splitarg'] = _arg, _commasplit, _splitarg
 
def Returned(_arg):
 _parse_to_reading('str ret,'+_arg.strip())
 return DataGlobal['ret'] 
 
def exception(excVal):
 global local_num, local_type, allException, DataGlobal, l_local_type
 excVal = str(excVal)
 if excVal.strip() == '':
  excVal = 'Exception by user'
 local_type = ''
 local_num = 0
 if not exc_hide and not _try_exc:
  try:
   if l_local_type.strip() == '':
    name = "module"
   else:
    name = l_local_type
   print('In "'+str(modulefile)+'", (line '+str(moduleline)+') at local "'+name+'":\n   '+str(excVal).replace('\n', '\\n')+'\nType "?" for more help')
  except Exception as e:
   pass
 if not exc_hide:
  allException.append(excVal)
  DataGlobal['ret'] = ''
  l_local_type = ''
  
def lexer(_command, _arg, _splitarg, _commasplit):
 global DataGlobal, DataRestrict
 try:
  if _command.strip() != '':
   exec('_Command.c__'+_command+'__("'+_arg+'", '+_splitarg+', '+_commasplit+')')
 except AttributeError:
  exception('"'+_command+'" is not a command, function, operator, data, literal or method')
 except ZeroDivisionError:
  exception('You can\'t divide by zero!')
 except SyntaxError:
  exception('"'+_command+'" is not a command, function, operator, data, literal or method')
 except Exception as e:
  exception('Python "'+str(e)+'"')
  
"""
 THIS IS A REAL BUILTIN FILE, CONTAINS: 
  COMMAND, FUNCTION, AND METHOD

 Function *Class
  as a High Grammar and can be used to 
  create a new keyword Internal
  
 type `help` for more information
"""
class _Command():
 """
 (C) Copyright 2019-2020 Muhammad Faran Aiki, All Rights Reserved.

 This class is to store all command, for example 
    `do` in FSCMD, you can call it in python by `c__do__`
    `print` in FSCMD, you can call it in python by `c__print__`
    ...
    
 You can get all command by using
    `dir(_Command)` or `all_command`
 """
 def c__setcommandasfunction__(_arg, _splitarg, _commasplit):
  global asFunction
  asFunction.extend([_c.lower() for _c in _commasplit])
 def c__scope__(_arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_line, l_scope_data
  if local_num:
   DataRestrict['local'] += this_rcmd+'\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   scope_line += 1
   local_num += 1
   if local_type == "":
    local_type = 'scope'
   try:
    l_scope_data = scope_data
    scope_data['name'] = _commasplit[0].strip().lower()
    scope_data['isVoidType'] = _arg.split(',', 1)[1] in TrueList
   except Exception as e:
    scope_data['name'] = _arg.strip().lower()
    scope_data['isVoidType'] = True
 def c__pyscope__(_arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_line, l_scope_data
  if local_num:
   DataRestrict['local'] += this_rcmd+'\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   scope_line += 1
   local_num += 1
   if local_type == "":
    local_type = 'pyscope'
   try:
    l_scope_data = scope_data
    scope_data['name'] = _commasplit[0].strip().lower()
    scope_data['isVoidType'] = _arg.split(',', 1)[1] in TrueList
   except Exception as e:
    scope_data['name'] = _arg.strip().lower()
    scope_data['isVoidType'] = True
 def c__void__(_arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_line, l_scope_data
  if local_num:
   DataRestrict['local'] += this_rcmd + '\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   scope_line += 1
   local_num += 1
   if local_type == "":
    local_type = 'void'
   l_scope_data = scope_data
 def c__pyvoid__(_arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_line, l_scope_data
  if local_num:
   DataRestrict['local'] += this_rcmd+'\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   local_num += 1
   scope_line += 1
   if local_type == "":
    local_type = 'pyvoid'
   l_scope_data = scope_data
 def c__dict__(_arg, _splitarg, _commasplit):
  try:
   current_dict = dict()
   if _arg.split(',', 1)[1].strip() == '':
    pass
   else:
    [current_dict.update({_parse_to_reading(s.split(':', 1)[0].strip()): _parse_to_reading(s.split(':', 1)[1].strip())}) for s in _arg.split(',', 1)[1].split(',')]
   DataGlobal[_commasplit[0]], DataGlobal['ret'] = current_dict, current_dict
  except IndexError:
   try:
    _arg.split(',', 1)[1]
    exception('Expression of a value (key) must be "key (command): value (command)" (for value), given only "key"')
   except IndexError:
    exception('"dict" need two argument, "data" and "value"')
 def c__for__(_arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_data, scope_line, l_scope_data
  if local_num:
   DataRestrict['local'] += this_rcmd+'\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   if local_type == "":
    local_type = 'for'
   scope_line += 1
   try:
    l_scope_data = scope_data
    _parse_to_reading(_arg.split(',', 1)[1].strip(), False)
    if local_type == 'for':
     scope_data['iter_variable'] = _commasplit[0]
     scope_data['variable'] = DataGlobal['ret']
   except KeyError:
    exception('Data is not exist "'+_commasplit[0]+'"')
    local_num = -1
   except IndexError:
    exception('"for" command need two argument, and scope code, (iteration_data, data)')
    local_num = -1
   local_num += 1
 def c__while__(_arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_data, scope_line, l_scope_data
  if local_num:
   DataRestrict['local'] += this_rcmd+'\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   if local_type == "":
    local_type = 'while'
   try:
    l_scope_data = scope_data
    if local_type == 'while':
     scope_data['variable'] = this_rcmd.strip().split(' ', 1)[1].strip()
    local_num += 1
   except IndexError as ie:
    exception('"while" command need one argument, "command"')
    local_num = 0
   scope_line += 1
 def c__if__(_arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_data, scope_line, l_scope_data
  if local_num:
   DataRestrict['local'] += this_rcmd+'\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   if local_type == "":
    local_type = 'if'
   try:
    l_scope_data = scope_data
    if local_type == 'if':
     _parse_to_reading(_arg.strip())
     if DataGlobal['ret'] in TrueList:
      scope_data['variable'] = True
     elif DataGlobal['ret'] in FalseList:
      scope_data['variable'] = False
     else:
      exception('Can\'t decide "false" or "true"')
      local_num = -1
    local_num += 1
   except IndexError:
    exception('"if" command need one argument, ${data})')
    local_num = 0
   scope_line += 1
 def c__def__(_arg, _splitarg, _commasplit):
  "create a command with python language, like: def helper, putchar help"
  try:
   exec('_Command.c__'+_commasplit[0].lower()+'__ = lambda _arg, _splitarg, _commasplit: exec(\'DataGlobal["_arg"], DataGlobal["_commasplit"], DataGlobal["_splitarg"], _argbefore, _commasplitbefore, _splitargbefore = _arg, _commasplit, _splitarg, DataGlobal["_arg"], DataGlobal["_commasplit"], DataGlobal["_splitarg"]; _parse_to_reading("'+Manipulator.stringifydef(_arg.split(',', 1)[1])+'"); DataGlobal["_arg"], DataGlobal["_commasplit"], DataGlobal["_splitarg"] = _argbefore, _commasplitbefore, _splitargbefore\')')
   try:
    AllCommand[modulefile] |= {_commasplit[0].lower().strip()}
   except:
    AllCommand[modulefile] = {_commasplit[0].lower().strip()}
  except IndexError:
   exception('"def" needs two argument (name, code)')
  except SyntaxError as se:
   exception('Python Exception "'+_commasplit[0]+'" caused SyntaxError')
  except Exception as e:
   exception(e)
 def c__try__(_arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_data, scope_line, l_scope_data
  if local_num:
   DataRestrict['local'] += this_rcmd+'\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   if local_type == "":
    local_type = 'try'
    local_num += 1
    scope_line += 1
 def c__catch__(_arg, _splitarg, _commasplit):
  global last_local, local_num, local_type, scope_data, scope_line, l_scope_data
  if local_num:
   DataRestrict['local'] += this_rcmd+'\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   if local_type == "":
    l_scope_data = scope_data
    scope_data['variable'] = _commasplit
    local_type = 'catch'
    local_num += 1
    scope_line += 1
 def c__new__(_arg, _splitarg, _commasplit):
  "create a new or replace existing command with argument: new <new-command>, <existing-command>. You can add --replace to make the <existing-command> replaced by <new-command>"
  global _Command, AllCommand
  try:
   exec('_Command.c__'+_commasplit[0].strip().lower()+'__ = _Command.c__'+_arg.split(',', 1)[1].strip().lower()+'__')
   _parse_to_reading('description '+_commasplit[0].strip().lower()+', same as "'+_arg.split(',', 1)[1].strip().lower()+'"')
   try:
    AllCommand[modulefile] |= {_commasplit[0].strip().lower()}
   except:
    AllCommand[modulefile] = {_commasplit[0].strip().lower()}
   if _arg.split(',', 1)[1].lower().strip() in AllAScope:
    AllAScope.append(_commasplit[0].lower().strip())
   if _arg.split(',', 1)[1].lower().strip() in AllScoped:
    AllScoped.append(_commasplit[0].lower().strip())
   if _arg.split(',', 1)[1].lower().strip() in asFunction:
    asFunction.append(_commasplit[0].lower().strip())
  except AttributeError:
   exception('"'+_arg.split(',', 1)[1].strip()+'" is not a command, function or method')
  except IndexError:
   exception('"new" need two argument, "new-command" and "command"')
  except SyntaxError:
   exception('"'+_arg.split(',', 1)[1]+'" is not a command, function or method')
 def c__license__(_arg, _splitarg, _commasplit):
  if modulefile == '$Console':
   print("""(C) Copyright 2019-2020 Muhammad Faran Aiki, All Rights Reserved""")
  else:
   DataGlobal['ret'] = '(C) Copyright 2019 Muhammad Faran Aiki, All Rights Reserved'
 def c__local__(_arg, _splitarg, _commasplit):
  "local is a scope command, and ended with end command, which mean local get stored in %local section (like function)"
  global last_local, local_num, local_type, scope_line
  if local_num:
   DataRestrict['local'] += this_rcmd + '\n'
   if local_type in AllAScope:
    local_num += 1
  if not in_comment and not local_num:
   last_local = _arg
   DataRestrict['local'] = ''
   DataRestrict[_arg] = ''
   local_num += 1
   scope_line += 1
   if local_type == "":
    local_type = "local"
 def c__do__(_arg, _splitarg, _commasplit):
  try:
   _parse_to_reading(_arg, ReplaceNewLine=False)
  except KeyError:
   exception('local "'+_arg+'" is not exist')
 def c__raise__(_arg, _splitarg, _commasplit):
  "raise an exception"
  exception(_arg)
 def c__cd__(_arg, _splitarg, _commasplit):
  "change directory"
  try:
   os.chdir(_arg)
  except FileNotFoundError:
   exception('Can\'t find "'+_arg+'" path/directory')
  except OSError:
   exception('Can\'t find "'+_arg+'" path/directory')
 def c__end__(_arg, _splitarg, _commasplit):
  "end is a command to end local scope, given argument will make '\\n' of command replaced with _arg"
  global last_local, local_num, local_type, my_function, l_local_type, scope_line, _try_exc, _handler_exc, allException, redir_catch, scope_data, l_scope_data
  if _arg.strip() == '':
   _arg = '\n'
  if local_num:
   local_num -= 1
  if local_num:
   DataRestrict['local'] += this_rcmd+'\n'
  if not local_num:
   DataRestrict['local'] = DataRestrict['local'].replace('\n', _arg).strip(_arg)
   if local_type == "local":
    local_type = ""
    DataRestrict[last_local] = DataRestrict['local']
   elif local_type == "try":
    local_type = ""
    befAllException = allException
    allException = []
    _code = DataRestrict['local'].strip()
    _try_exc = True
    _parse_to_reading(_code, ReplaceNewLine=False)
    _try_exc = False
    if len(allException) > 0:
      try:
       ber, bex = DataGlobal['_error'], DataGlobal['_exception']
       bet = dict(zip(redir_catch, [DataGlobal[r] for r in redir_catch]))
      except:
       pass
      if len(allException) > 1:
       DataGlobal['_error'], DataGlobal['_exception'] = (allException, allException)
       for c in redir_catch:
        DataGlobal[c] = allException
      else:
       DataGlobal['_error'], DataGlobal['_exception'] = (''.join(allException).strip(), ''.join(allException).strip())
       for c in redir_catch:
        DataGlobal[c] = ''.join(allException).strip()
      _parse_to_reading(_handler_exc, ReplaceNewLine=False)
      try:
       DataGlobal['_error'], DataGlobal['_exception'] = ber, bex
       for c in redir_catch:
        DataGlobal[c] = bet[c]
      except:
       pass
    allException = befAllException
   elif local_type == "catch":
    local_type = ""
    _handler_exc = DataRestrict['local'].strip()
    redir_catch = scope_data['variable']
   elif local_type == "void":
    local_type = ""
    exec('_Command.c__'+last_local.lower().strip()+'__ = lambda _arg, _splitarg, _commasplit: exec(\'DataGlobal["_arg"], DataGlobal["_commasplit"], DataGlobal["_splitarg"], _argbefore, _commasplitbefore, _splitargbefore = _arg, _commasplit, _splitarg, DataGlobal["_arg"], DataGlobal["_commasplit"], DataGlobal["_splitarg"]; _parse_to_reading("'+Manipulator.stringifydef(DataRestrict['local'].replace('\n', '\\n'))+'", ReplaceNewLine=False); DataGlobal["_arg"], DataGlobal["_commasplit"], DataGlobal["_splitarg"] = _argbefore, _commasplitbefore, _splitargbefore\')')
    try:
     AllCommand[modulefile] |= {last_local.lower().strip()}
    except:
     AllCommand[modulefile] = {last_local.lower().strip()}
   elif local_type == "pyvoid":
    local_type = ""
    exec('_Command.c__'+last_local.lower().strip()+'__ = lambda _xarg, _xsplitarg, _xcommasplit: exec("_arg, _commasplit, _splitarg = _xarg, _xcommasplit, _xsplitarg\\n'+Manipulator.stringifypydef(DataRestrict['local'].replace('\n', '\\n'))+'")')
    try:
     AllCommand[modulefile] |= {last_local.lower().strip()}
    except:
     AllCommand[modulefile] = {last_local.lower().strip()}
   elif local_type == "for":
    iter_variable = scope_data['iter_variable']
    variable = scope_data['variable']
    current_command = DataRestrict['local']
    try:
     last = DataGlobal[iter_variable]
    except:
     last = None
    def my_function(data):
     DataGlobal[iter_variable] = data
     _parse_to_reading(current_command, ReplaceNewLine=False)
    [my_function(data) for data in variable]
    if last == None:
     del DataGlobal[iter_variable]
    else:
     DataGlobal[iter_variable] = last
   elif local_type == 'while':
    local_type = ""
    variable = scope_data['variable']
    try:
     data = _parse_to_reading(variable, False) in TrueList
     current_command = DataRestrict['local']
     while data:
      _parse_to_reading(current_command, ReplaceNewLine=False)
      data = _parse_to_reading(variable, False) in TrueList
    except Exception as e:
     pass
   elif local_type == "if":
    local_type = ""
    variable = scope_data['variable']
    _code = DataRestrict['local']
    if variable:
     _parse_to_reading(_code, ReplaceNewLine=False)
   elif local_type == 'scope':
    local_type = ""
    name = scope_data['name']
    isVoidType = scope_data['isVoidType']
    AllScoped.append(name)
    AllCScope[name] = DataRestrict['local']
    if isVoidType:
     AllAScope.append(name)
    def _o(_arg, _splitarg, _commasplit):
     scope_creator(name, _arg, _splitarg, _commasplit)
    exec('_Command.c__'+name+'__ = _o')
   elif local_type == 'pyscope':
    local_type = ""
    name = scope_data['name']
    isVoidType = scope_data['isVoidType']
    AllScoped.append(name)
    AllPScope[name] = DataRestrict['local']
    if isVoidType:
     AllAScope.append(name)
    def _o(_arg, _splitarg, _commasplit):
     scope_creator(name, _arg, _splitarg, _commasplit)
    exec('_Command.c__'+name+'__ = _o')
   elif local_type in AllPScope:
    codeFrom = local_type
    local_type = ""
    _code = DataRestrict['local'].replace('\n', '\\n')
    exec(AllPScope[codeFrom])
   elif local_type in AllCScope:
    codeFrom = local_type
    local_type = ""
    arg = DataGlobal['_arg']
    cag = DataGlobal['_commasplit']
    spl = DataGlobal['_splitarg']
    try:
     bef = DataGlobal['_code']
    except:
     pass
    DataGlobal['_arg'] = scope_data['_arg']
    DataGlobal['_splitarg'] = scope_data['_splitarg']
    DataGlobal['_commasplit'] = scope_data['_commasplit']
    DataGlobal['_code'] = DataRestrict['local'].replace('\n', '\\n')
    _parse_to_reading(AllCScope[codeFrom], ReplaceNewLine=False)
    try:
     DataGlobal['_code'] = bef
    except:
     del DataGlobal['_code']
    DataGlobal['_arg'] = arg
    DataGlobal['_commasplit'] = cag
    DataGlobal['_splitarg'] = spl
   last_local = ''
   local_type = ''
   scope_line = 0
   scope_data = {}
 def c__access__(_arg, _splitarg, _commasplit):
  try:
   DataGlobal['ret'] = {**locals(), **globals()}[_arg]
  except KeyError:
   exception('Data is not exist in python runtime "'+_arg+'"')
 def c__vars__(_arg, _splitarg, _commasplit):
  "show variables (int, str)"
  if modulefile == '$Console':
   print('\n'.join([var+', "'+str(DataGlobal[var])+'" type '+str(type(DataGlobal[var])).split("'")[1] for var in DataGlobal]))
  else:
   DataGlobal['ret'] = DataGlobal
 def c__locals__(_arg, _splitarg, _commasplit):
  if modulefile == '$Console':
   print('\n'.join([s for s in DataRestrict]))
  else:
   DataGlobal['ret'] = DataRestrict
 def c__labels__(_arg, _splitarg, _commasplit):
  "show all labels including builtin label"
  if modulefile == '$Console':
   print('\n'.join([l+', line '+str(SectionLabel[l]) for l in SectionLabel]))
  else:
   DataGlobal['ret'] = SectionLabel
 def c__pyload__(_arg, _splitarg, _commasplit):
  "python load (import method, function in python module (usually for pydef or pyexec))"
  for com in _commasplit:
   try:
    exec('global '+com+'\n'+com+' = importlib.import_module("'+com+'")')
   except Exception as e:
    exception(e)
  DataGlobal['ret'] = ''
 def c__pyexec__(_arg, _splitarg, _commasplit):
  "python execution (execute script with exec() command)"
  try:
   _ = eval(_arg.strip())
   if _ is not None:
    DataGlobal['ret'] = _
  except Exception as e:
   exception(e)
 def c__pydef__(_arg, _splitarg, _commasplit):
  "create a command with python language, like: pydef help, help()"
  try:
   exec('_Command.c__'+_commasplit[0].lower()+'__ = lambda _xarg, _xsplitarg, _xcommasplit: exec("_arg, _commasplit, _splitarg = _xarg, _xcommasplit, _xsplitarg\\n'+_arg.split(',', 1)[1].strip().replace('\\"', '\\\\"').replace("\\'", "\\\\'").replace("\"", '\\"').replace('\'', '\\\'').replace('\n', '\\n')+'")')
   try:
    AllCommand[modulefile] |= {_commasplit[0].lower().strip()}
   except:
    AllCommand[modulefile] = {_commasplit[0].lower().strip()}
  except IndexError:
   exception('"pydef" needs two argument (name, python code)')
  except SyntaxError as se:
   exception('Python Exception "'+_commasplit[0]+'" caused SyntaxError "'+str(se)+'"')
  except Exception as e:
   exception(e)
 def c__list__(_arg, _splitarg, _commasplit):
  "list command, make a list of word with argument: list ${name}, ${ordered-data}. accessed with index and ordered"
  global DataGlobal
  try:
   if _arg.split(',', 1)[1].strip() == '':
    DataGlobal[_commasplit[0]] = []
   else:
    DataGlobal[_commasplit[0]] = [_parse_to_reading(i) for i in _arg.split(',', 1)[1].strip().split(',')]
  except IndexError:
   try:
    DataGlobal[_commasplit[0]] = []
   except:
    exception('"list" at least need one argument')
  except Exception as e:
   print(_arg)
  try:
   DataGlobal['ret'] = DataGlobal[_commasplit[0]]
  except:
   pass
 def c__tuple__(_arg, _splitarg, _commasplit):
  "tuple command, make a list of word with argument: tuple ${name}, ${ordered-data}. accessed with index and ordered but can't be changed by index"
  global DataGlobal
  try:
   if _arg.split(',', 1)[1].strip() == '':
    DataGlobal[_commasplit[0]] = ()
   else:
    DataGlobal[_commasplit[0]] = tuple([_parse_to_reading(i) for i in _arg.split(',', 1)[1].strip().split(',')])
  except IndexError:
   try:
    DataGlobal[_commasplit[0]] = ()
   except:
    exception('"tuple" at least need one argument')
  except Exception as e:
   print(_arg)
  try:
   DataGlobal['ret'] = DataGlobal[_commasplit[0]]
  except:
   pass
 def c__unite__(_arg, _splitarg, _commasplit):
  "unite command, make a unite of word with argument: unite ${name}, ${data}. set can't be accessed with index and unordered"
  global DataGlobal
  try:
   if _arg.split(',', 1)[1].strip() == '':
    DataGlobal[_commasplit[0]] = {}
   else:
    DataGlobal[_commasplit[0]] = set([_parse_to_reading(a.strip()) for a in _arg.split(',', 1)[1].split(',')])
  except IndexError:
   try:
    DataGlobal[_commasplit[0]] = {}
   except:
    exception('"unite" at least need one argument')
  except TypeError:
   exception('"unite" is not hashable')
  try:
   DataGlobal['ret'] = DataGlobal[_commasplit[0]]
  except:
   pass
 def c__load__(_arg, _splitarg, _commasplit):
  "import/load file from based-module folder, ex: load loop, regex, math"
  global modulefile, moduleline, docstring, allComment, history_com, csp_com
  bAllComment = allComment
  bhistory_com = history_com
  history_com = []
  if _arg.strip().lower() == '*':
   _commasplit = [a for a in os.listdir(loadpath) if a.endswith('.fcm') and os.path.isfile(loadpath+a)]
  for _c in _commasplit:
   if _c not in AllCommand:
    try:
     executefile(loadpath+_c+'.fcm', True)
     docstring[_c] = allComment
    except (FileNotFoundError, OSError):
     try:
      executefile(loadpath+_c, True)
     except (FileNotFoundError, OSError):
      exception('Module is not exist "'+_c+'"')
  allComment = bAllComment
  history_com = bhistory_com
  csp_com = ''
  DataGlobal['ret'] = ''
 def c__import__(_arg, _splitarg, _commasplit):
  "import/load from near, this folder, ex: import Files.fcm"
  global modulefile, moduleline, docstring, allComment, history_com, csp_com
  bAllComment = allComment
  bhistory_com = history_com
  history_com = []
  if _arg.strip().lower() == '*':
   _commasplit = [a for a in os.listdir() if a.endswith('.fcm') and os.path.isfile(a)]
  for _c in _commasplit:
   if _c not in AllCommand:
    try:
     executefile(os.path.abspath('')+'\\'+_c)
    except (FileNotFoundError, OSError):
     try:
      executefile(os.path.abspath('')+'\\'+_c+'.fcm')
      docstring[_c] = allComment
     except (FileNotFoundError, OSError):
      exception('File is not exist "'+_c+'"')
  allComment = bAllComment
  history_com = bhistory_com
  csp_com = ''
  DataGlobal['ret'] = ''
 def c__write__(_arg, _splitarg, _commasplit):
  "write a file with argument write <file>, <content>"
  try:
   open(_commasplit[0], 'a', encoding='utf-8').write(_arg.split(',', 1)[1].strip()+'\n')
  except PermissionError:
   exception('Access denied by user (Need Administration to Write)')
  except IndexError:
   exception('"write" need two argument, "file" and "text"')
 def c__float__(_arg, _splitarg, _commasplit):
  "float data type (friend of integer), example: float a, 1.3 (set a to 1.3)"
  try:
   DataGlobal[_commasplit[0]] = float(str(_parse_to_reading(_arg.split(',', 1)[1])).replace(' ', ''))
  except IndexError:
   try:
    DataGlobal[_commasplit[0]] = 0.0
   except:
    exception('"float" at least need one argument')
  except ValueError:
   exception("'"+_arg.split(',', 1)[1].replace(' ', '')+'\' is not float type')
  try:
   DataGlobal['ret'] = DataGlobal[_commasplit[0]]
  except:
   pass
 def c__eval__(_arg, _splitarg, _commasplit):
  try:
   _parse_to_reading(_arg.split(',', 1)[1].strip())
   _parse_to_reading(_commasplit[0]+' '+str(DataGlobal['ret']))
  except:
   pass
 def c__label__(_arg, _splitarg, _commasplit):
  "create a label, based label is end, start"
  SectionLabel[_arg.strip(':')] = moduleline
 def c__input__(_arg, _splitarg, _commasplit):
  "read user input with argument: input <prompt> and return it with value \"ret\""
  _spaced = ' '
  if _arg.strip() == '':
    _spaced = ''
  try:
   DataGlobal['ret'] = input(_arg+_spaced)
  except:
   pass
 def c__goto__(_arg, _splitarg, _commasplit):
  "goto command, reverse command line to which label or line to go"
  global moduleline
  try:
   moduleline = int(_arg)-1
  except Exception as e:
   try:
    if _arg in SectionLabel:
     moduleline = SectionLabel[_arg.strip(':')]
    else:
     exception("No label named '"+_arg+"'")
   except:
    pass
 def c__int__(_arg, _splitarg, _commasplit): #bint
  "integer command that set a new integer memory with argument: int <memory>, <value>"
  global DataGlobal
  try:
   DataGlobal[_commasplit[0]] = int(str(_parse_to_reading(_arg.split(',', 1)[1])).replace(' ', ''))
  except IndexError:
   try:
    DataGlobal[_commasplit[0]] = 0
   except:
    exception('"int" at least need one argument')
  except ValueError:
   exception("'"+str(DataGlobal['ret'])+"' is not a based integer")
  try: 
   DataGlobal['ret'] = DataGlobal[_commasplit[0]]
  except:
   pass
 def c__str__(_arg, _splitarg, _commasplit): #bstr
  "string command that set a new string memory with argument: str <memory>, <value>"
  global DataGlobal
  try:
   DataGlobal[_commasplit[0]] = eval("'"+_arg.split(',', 1)[1]+"'")
  except IndexError:
   try:
    DataGlobal[_commasplit[0]] = ''
   except:
    exception('"str" at least need one argument')
  except SyntaxError:
   try:
    DataGlobal[_commasplit[0]] = eval("'"+_arg.split(',', 1)[1].replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")+"'")
   except:
    DataGlobal[_commasplit[0]] = _arg.split(',', 1)[1]
  try:
   DataGlobal['ret'] = DataGlobal[_commasplit[0]]
  except:
   pass
 def c__description__(_arg, _splitarg, _commasplit):
  "make a command describable"
  try:
   AllHelper[_commasplit[0].strip().lower()] = _arg.split(',', 1)[1]
  except IndexError:
   exception('"description" need two argument, "command (single)" and "description"')
 def c__help__(_arg, _splitarg, _commasplit):
  "are you kidding me? just type help <argument> already!"
  if _commasplit != []:
   for _help in _commasplit:
    try:
     try:
      if _help in eFirstOperator:
       print(_help+' '+FirstOperator[_help].strip()+'\n  '+AllHelper['efirstoperator:'+_help.lower()], flush=True)
      elif _help in FirstOperator:
       print(_help+' '+FirstOperator[_help].strip()+'\n  '+AllHelper['firstoperator:'+_help.lower()], flush=True)
      if _help in fLastOperator:
       print(_help+' '+LastOperator[_help].strip()+'\n  '+AllHelper['flastoperator:'+_help.lower()], flush=True)
      elif _help in eLastOperator:
       print(_help+' '+LastOperator[_help].strip()+'\n  '+AllHelper['elastoperator:'+_help.lower()], flush=True)
      elif _help in LastOperator:
       print(_help+' '+LastOperator[_help].strip()+'\n  '+AllHelper['lastoperator:'+_help.lower()], flush=True)
      if _help in SecOperator:
       print(_help+' '+SecOperator[_help].strip()+'\n  '+AllHelper['secondoperator:'+_help.lower()], flush=True)     
      if tuple(_help.split(' ')) in AbsOperator:
       print('"'+_help+'" '+AbsOperator[tuple(_help.split(' '))].strip() + '\n  '+AllHelper['absoluteoperator:'+_help.lower()], flush=True)
       print('  You can execute this operator if your command starts with "'+tuple(_help.split(' '))[0]+'" and ends with "'+tuple(_help.split(' '))[1]+'"')
      if _help not in FirstOperator and _help not in SecOperator and _help not in LastOperator and not tuple(_help.split(' ')) in AbsOperator:
       print(_help+' _arg, _splitarg, _commasplit\n  '+AllHelper[_help.lower()], flush=True)
      raised=False
     except Exception as e:
      raised=True
     try:
      if _help.endswith('.fcm') and not _help.startswith('$'):
       print('Here is the docstring from the module\n '+'\n '.join(docstring[_help].split('\n'))+'\n\nAll command from ', end='')
       _shower_some_command(_help)
      elif _help.strip().lower() == 'builtin' or _help.strip().lower() == 'built-in':
       print('Here is the docstring from the module\n '+'\n '.join(docstring['builtin'].split('\n'))+'\n\nAll command from ', end='')
       _shower_some_command("builtin/standard command (lexer.py)")
      elif _help.strip().lower() == '$console':
       print('Main console, type `getListCommand $console` for console command information')
      else:
       print('Here is the docstring from the module\n '+'\n '.join(docstring[_help].split('\n'))+'\n\nAll command from ', end='')
       _shower_some_command(_help+'.fcm')
       raised=False
     except:
      if raised:
       raised=True
     try:
      _shower_help_special(_help)
      raised=False
     except:
      if raised:
       raise
    except:
      exception("\""+_help+'" is not describable (does not have description)')
  elif modulefile == '$Console':
   print("""
(C) Copyright 2019 Muhammad Faran Aiki, All Rights Reserved

YOU ARE USING A 100% STILL DEVELOPING/IMPROVING FSCMD! 

Since this is version 0.1 and developed by one developer, 
 Math, Algorithm, Booleans is still imperfect, for case of:
  More Logic gate
  More Syntax beautification
  More Finished bug
  More Mathematics (Integral, Complex Number, Graph) .etc

My really first big project that got published (I think so ...)
I create this (alone) in 1/2 year (2019-2020)

Distribution of Faran Standard Command (Fancy Style Command) and Faran Command (FSCMD Module) [FSCMD and FCM]
 *Please guys, this project is hard to make*

I'm "Muhammad Faran Aiki", the Founder and Owner of this programming language (I don't know if this profitable, but I don't care :D)

"fscmd" or "osfcm/fcm" is a multi-paradigm (still working on the OOP cause it's hard), multi-style, multi-language, and multi-programming.
It's used for basic and advanced instruction with high interpretation and low interpretation

"fscmd" or "osfcm/fcm" is an universal (kind-like) object-oriented (still working) + (kind-like) procedural, no. it's a whole new programming language! (Fancy Style Programming)
and Open-Source programming language that created by Muhammad Faran Aiki in Indonesia/Depok 
at 2019, and I develop this JUST for fun (actually for helping people too! help to create better style and communication)

"fscmd" or "osfcm/fcm" the language is created by a single person (solo developer), 
and if you claim it you are the worst (lol), really really worst. (hehe)

"fscmd" or "osfcm/fcm" are working well with Python and 
other programming language.

"fscmd" is still in development, which is sucks (:D)

Does this software/distribution for free? Of course
it's for free for all! and you can donate too :D #I don't know where to get moneys, it sucks to be a kid

Since my deadline is at 1 January 2020,
 So of course there's many bugs in here

I created this because the first time I want t create cmd-like but ended up
creating a new programming language. You can use the programming language
to create software, apk or module (or anything you like, maybe)

You can even send your own module! And I will credit you by Copyrighting/Licensing the module
if you give it to me by email me (look at the bottom)

The "osfcm/fcm" script can be converted to python using:
 fcmpy.py (located at include directory)
  with function: Complete() [you can search it up]
 or using other software

FSCMD can be used to a new programming language, using:
 FSCMD itself and help from Python (3.7.2)
 The instruction to make a new programming language is available online or ...
 
The instruction command, lexer are editable and have many version.
You are using the real version of the lexer (Faran Version).

THE REAL IMPORTANT COMMAND IN FSCMD::
 1. eval, exec (help eval, exec)
 2. var (help var)
 3. putchar and print (help putchar, print)
 4. pydef and def (help pydef, def)
 5. int, str, float, list, unite (help int, str, float, list, unite)
 6. add, mult, modl (help add, mult, modl)
 7. isEqual, isIn, isGreater, isLower (all command in statement.fcm)
 8. local command
 9. void, pyvoid .etc
 10. operator
 # Actually all command are important

Procedure File:
 fscmd->other->Procedure.txt

Here is defined Variable (Only at lexer.py) ->
 1. _arg ("") replacement for _arg
 2. _commasplit ("") replacement for _commasplit
 3. _splitarg ("") replacement for _splitarg
 4. _argv -> Argument Vector (same as C, Python .etc)
 5. _argc -> Argument Count (same as C)
 6. _argvs -> Argument Vector as String -> ['a', 'b'] -> 'a b'
 7. _argvc -> Argument Vector per Comma split -> 'a, b, c' -> ['a', 'b', 'c']
 8. _newline -> '\\\\n' [replace newline with "\n"]
 9. _spacebar -> ' '
 10. _dollar -> '$'
 11. ret -> Return value. Use "return" to set this variable. for example: var name, reversestr Faran

Here is the "How" to do ...

How to do an if statement and unless?:
 if <True> | <False> (execute if true, basically is a command)
  // do something here
 unless <True> | <False> (execute if false, basically is a command)
  // do something here
  
How to use try and catch an error?
 NOTE:: use catch first, then try. for example:
 catch 
  print ${_error}
 end
 try
  faranIsCool
 end  
 // "faraniscool" is not a command ...
 
How to create a class?: <- Still in Development
 class ${class-name}, <argument>....
 
How to create object with defined class? <- Still in Development
 obj ${object-name}, ${object-class}, <argument>..
 
How to add a function to a defined class? <- Still in Development
 add_func ${class-name}, ${function-name}, ${python-code}

How to call a Data? Length of Data, Real Data, Listed Data?:
 Use '$(Data)' for length of data, example script:
  int a, 1 234 567 890
  putchar $(a)
  // the output is 10 since integer will be converted to string and then converted to size
 Use '${Data}' for value or real of data, example script:
  str unpname,uido Van Rossu
  putchar G${unpname}m
  // the output is Guido Van Rossum
 Use '$<Data>' for list typed data to string
  list n, 1, 2, 3
  print ${n} 
  // ["1", "2", "3"]
  print $<n>
  // 1, 2, 3

How to do a looping?
 You can use `for` or `while` but they are still in development!
 You can type "?for" or "?while"

How to do a Comment?:
 Use "//" for a single line comment or
 Use "'''" or '\"""' for a multi line comment and for documenting file [docstring] (?math <- display information about math and the docstring)
 NOTE::
  Remember that comment can't be placed in command section (putchar a // this is not comment) 
  Remember that multi-line comment ALWAYS has first three '"' or "'", if not then there will be an error
How to add a operator?
 Type "?operator" for more help

How to create a Python Code Command?:
 use 'pydef' for command type('help pydef') or 'pyvoid'
 And if you want to create a multiline command, use local (type 'help local')
 Or the best way, you can use 'pyvoid' or 'pvoid'

How to Describe a command?
 using "description" or "desc", you can create a 
 description of a command with argument:
  desc NAME, DESCRIPTION
 and you can remove it using "descremove"
 
How to call a Local?:
 if you want to call a local, then use
  %{local-name}
 this will call the content of local (type 'help end' or 'help local')

What is '#[...]', '$[...]' and '%[...]' or another scripting special?:
 #... -> special case:
  #[...] will execute the '...' command and then returned to that same position,
   load math
   print #[calc 1+23]
   // this will print out 24 because the '#[calc 1+23]' is changed with 1+23 = 24
  #{...} will execute the '...' but only one '#{...}' per command line
   print #{#[1 + 2]}
   // this will print out 3
  #(...) same as #[...], but more often to use this at operator
 %... -> protected data case:
  %{...} will get the protected data from DataRestrict (local),
   local isEnv
    print Hello, World!
    print Hi
   end
   print %{isEnv}
   // result print Hello, World!\n...
 $... -> open data case:
  As Explained before,
   ${...} -> as string
   $(...) -> as length
   $<...> -> as listed

Note that if you want to create a data using '->' or '=' command, please use `my`, for example::
 x = set 
 // this will raise an error, better use
 x = mySet 
 // or 
 x = ... <- symbol

In FSCMD, There's a big difference between FUNCTION and COMMAND,
 FUNCTION will not called IF there's operator [especially "SecondOperator"] and ONLY will be called if command line has that function
 COMMAND will always called IF the command line starts with it

Operator in FSCMD, you can create it too!
 you can type `help operator` for more help about operator

Eval, Exec and other things that are really important for single line code:
 Eval   : Eval putchar, input To Putchar
 Exec   : Exec Input Command:
 Return : Return ${n}

Void, Pyvoid:
 void is equal to
  local
   ...
  end
  def <name>, %{local}
 pyvoid is equal to
  local 
   ...
  end
  pydef <name>, %{local}

Extraction, used for create an unique string, for example [TAB]:
 x = extract \\t
 print ${x}1
 //      1
  
See "comparison.txt" or type "?comparison" for 
 Pros and Cons FSCMD
""")
   _shower_command()
   print("Classes are defined here:\n")
   _shower_class()
   print("""For more information, type ["help <something>" -> "?<something>"]:
 "help <command>"
 "help <module>"
 "help <operator>"
 "help <special-thing>"
Or see readme.txt/help.txt in
 this Folder (fscmd)
  
If you need more helper, any question or a bug, feel free to ask, report or give me in (and sure, the credit goes to you [if you find or solve the bug]):
 My Youtube, Discord    : Faran2007
    Instagram           : faranthemastery
    Facebook            : muhammadfaranaiki
    Gmail               : abang.faran.aiki@gmail.com | faran.helper.acc@gmail.com (RECOMMENDED)

Look up! Read the start to the end,
 If you are still confused, You can find and search FSCMD Tutorial too!
 
And Remember, 
 FSCMD does not only comes with free-syntax or free-function
  BUT
 Operator (!, +, -=, ~=)
     ||
 Type "?operator"
""")
  else:
   DataGlobal['ret'] = 'help'
 def c__typeof__(_arg, _splitarg, _commasplit):
  "typeof object"
  try:
   DataGlobal['ret'] = type(_parse_to_reading(_arg)).__name__
  except KeyError:
   exception('Data is not exist "'+_v+'"')
 def c__run__(_arg, _splitarg, _commasplit):
  "run a file"
  os.system(_arg)
 def c__read__(_arg, _splitarg, _commasplit):
  "read and return value to $ret, expected argument is read <file>, but you can add --return and --show"
  try:
   DataGlobal['ret'] = open(_arg, 'r').read()
  except FileNotFoundError:
   try:
    exception('File is not exist "'+_splitarg[0]+'"')
   except:
    DataGlobal['ret'] = input()
  except PermissionError:
   exception('Access denied by user (Need Administrator)')
 def c__exit__(_arg, _splitarg, _commasplit):
  "exit and return status"
  if not _arg.strip() == '':
   print('Exit with status "'+_arg+'"')
  sys.exit()
 def c__prompt__(_arg, _splitarg, _commasplit):
  global _cursor
  "change cursor/prompt in $Console"
  if _arg.strip() != '':
   _cursor = _arg
  else:
   _cursor = ''
  if _arg.lower() == '%path%':
   _cursor = _std_cursor
 def c__del__(_arg, _splitarg, _commasplit):
  "delete a file by parameter del <file>"
  try:
   for file in _commasplit: os.remove(file)
  except FileNotFoundError as fne:
   exception('File is not exist "'+file+'"')
  except PermissionError:
   exception('Access denied by user (Need Administrator) or file is used')
 def c__exec__(_arg, _splitarg, _commasplit):
  "exec is not same as pyexec"
  _parse_to_reading(_parse_to_reading(_arg))
 def c__wait__(_arg, _splitarg, _commasplit):
  try:
   time.sleep(float(_arg))
  except ValueError:
   exception('"'+_arg+'" is not a based integer or float')
 def c__bool__(_arg, _splitarg, _commasplit):
  try:
   if _arg.split(',', 1)[1].strip().lower() in TrueList:
    DataGlobal[_commasplit[0]] = True
   elif _arg.split(',', 1)[1].strip().lower() in FalseList:
    DataGlobal[_commasplit[0]] = False
   else:
    DataGlobal[_commasplit[0]] = DataTypes.null()
  except IndexError:
   exception('"bool" need two argument, "data" and "value"')
 def c__pass__(_arg, _splitarg, _commasplit):
  "pass"
 def c__set_stdout__(_arg, _splitarg, _commasplit):
  sys.stdout = _parse_to_reading(_arg)
 def c__set_stdin__(_arg, _splitarg, _commasplit):
  sys.stdin = _parse_to_reading(_arg)
 def c__openf__(_arg, _splitarg, _commasplit):
  try:
   if len(_commasplit) == 1:
    DataGlobal['ret'] = open(_arg, 'a+')
   else:
    try:
     DataGlobal['ret'] = [open(_f, 'a+') for _f in _commasplit]
    except (FileNotFoundError, OSError):
     exception('Some file is not exist')
    except (PermissionError):
     exception('Some file doesn\'t have permission to access')
  except (FileNotFoundError, OSError):
   exception('File is not exist "'+_arg+'"')
  except (PermissionError):
   exception('Can\'t access file "'+_arg+'"')
 def c__dir__(_arg, _splitarg, _commasplit):
  "show current directory, either --return or --show"
  if modulefile == '$Console' or '-s' in _splitarg and '-r' not in _splitarg or '--show' in _splitarg and not '--return' in _splitarg:
   print('\nThis Directory ("'+os.path.abspath('')+'")\n')
   totalFile = 0
   totalFolder = 0
   for y in os.listdir():
    IsDir = 'File'
    if os.path.isdir(y):
     IsDir = 'Folder'
     totalFolder += 1
    else:
     totalFile += 1
    print('\t['+IsDir+']  \t'+y+'\t')
   print('\n\t\tFile: '+str(totalFile)+'\tFolder: '+str(totalFolder)+'\n')
  else:
   DataGlobal['ret'] = os.listdir()
   
class _escape():
 newline = '\n' 

class _FSCMD_():
 pass

AllCommand['builtin/standard command (lexer.py)'] = set([_c.split('c__', 1)[1].rstrip('__') for _c in dir(_Command) if _c.startswith('c__')])

""" Start Initializing for normal FSCMD """
_parse_to_reading('load newkey')
history_com = []
DataRestrict = {}

""" Initializing for normal python """
do = _parse_to_reading
evaluate = _parse_to_reading

""" (C) Created by Muhammad Faran Aiki """
if __name__ == '__main__':
    _parse_to_reading('help')
    input()
else:
    isAutoRepln  = False
    _using_fscmd = True
