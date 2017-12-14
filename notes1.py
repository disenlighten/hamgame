#Multiple choice notes 12/10/17

# read entire question into an array
question = """T1A01 (C) [97.1]
... Which of the following is a purpose of the Amateur Radio Service as stated in the FCC rules and regulations?
... A. Providing personal radio communications for as many citizens as possible
... B. Providing communications for international non-profit organizations
... C. Advancing skills in the technical and communication phases of the radio art
... D. All of these choices are correct """
# define a dictionary for the question
dct = {}

#Make another array for each line of the question
lines = question.split("\n")
>>> lines

['T1A01 (C) [97.1]', 'Which of the following is a purpose of the Amateur Radio Service as stated in the FCC rules and regulations?', 'A. Providing personal radio communications for as many citizens as possible', 'B. Providing communications for international non-profit organizations', 'C. Advancing skills in the technical and communication phases of the radio art', 'D. All of these choices are correct ']

#define a variable with the correct answer
dct["correct_ans"] = re.split(r'[()]',lines[0])[1]
#definte a variable with the Question itself
dct["question"] = lines[1]
#define variables for each answer
dct["a"] = lines[2]
dct["b"] = lines[3]
dct["c"] = lines[4]
dct["d"] = lines[5]

# set the ~ delimiter as a variable
delim = "~" 

# Test of for/in - Bad
with open("/Users/james/Downloads/2014-2018 Tech Pool.txt") as f:
    for row in f: 
        if "~" in f:    
            print(f)  


# Bad
with open("/Users/james/Downloads/2014-2018 Tech Pool.txt") as f:
data = f.read().splitlines()
  for row in data:
    if "~" in f: 
    newlist = [row[i:i + 5] for i in range(0, len(data), 5)

#bad
f = open('/Users/james/Downloads/2014-2018 Tech Pool.txt','r')
x = f.readlines().splitlines()


#FAIL
In [42]: with open("/Users/james/Downloads/2014-2018 Tech Pool.txt") as f:
    ...:     for line in f:
    ...:         if "~" in line:
    ...:             for i in next(5): 
    ...:                 print(i)
    ...:                 
    ...:                 
    ...:             
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-42-2c9f92fb5060> in <module>()
      2     for line in f:
      3         if "~" in line:
----> 4             for i in next(5):
      5                 print(i)
      6 

TypeError: 'int' object is not an iterator

#FAILL
In [44]: with open("/Users/james/Downloads/2014-2018 Tech Pool.txt") as f:
    ...:     for line in f:
    ...:         if "~" in line:
    ...:             for i in range(5): 
    ...:                 print(line[i])
    ...:                 
    ...:                 
    ...:                 
    ...:                 
    ...:             
~
~


---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-44-c9a2b617da74> in <module>()
      3         if "~" in line:
      4             for i in range(5):
----> 5                 print(line[i])
      6 
      7 

IndexError: string index out of range

In [45]: i
Out[45]: 3

#nice formatting

In [103]: f = open('/Users/james/Downloads/2014-2018 Tech Pool.txt','r')
     ...: readLines = f.readlines()
     ...: Types = [line.split("\n") for line in readLines]
     ...: 
     ...: questions = []
     ...: for lineno, member in Types: 
     ...:     print(member)
     ...:     print(lineno)
     ...:     
     ...:             
     ...:             
     ...:         


In [114]: for e in Types[1:5:]:
     ...:     print(e)
     ...:     
['', '']
['T1A - Amateur Radio Service: purpose and permissible use of the Amateur Radio Service; operator/primary station license grant; where FCC rules are codified; basis and purpose of FCC rules; meanings of basic terms used in FCC rules; interference; spectrum management', '']
['', '']
['T1A01 (C) [97.1]', '']

In [115]: for e in Types[3:8:]:
     ...:     print(e)
     ...:     
     ...:     
['', '']
['T1A01 (C) [97.1]', '']
['Which of the following is a purpose of the Amateur Radio Service as stated in the FCC rules and regulations?', '']
['A. Providing personal radio communications for as many citizens as possible', '']
['B. Providing communications for international non-profit organizations', '']

In [116]: for e in Types[4:10:]:
     ...:     print(e)
     ...:     
     ...:     
     ...:     
['T1A01 (C) [97.1]', '']
['Which of the following is a purpose of the Amateur Radio Service as stated in the FCC rules and regulations?', '']
['A. Providing personal radio communications for as many citizens as possible', '']
['B. Providing communications for international non-profit organizations', '']
['C. Advancing skills in the technical and communication phases of the radio art', '']
['D. All of these choices are correct ', '']

In [117]: for e in Types[4:10:]:
     ...:     print(e)[0]
     ...:     
     ...:     
     ...:     
     ...:     
['T1A01 (C) [97.1]', '']
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-117-e7ee0f38e934> in <module>()
      1 for e in Types[4:10:]:
----> 2     print(e)[0]
      3 
      4 
      5 

TypeError: 'NoneType' object is not subscriptable


In [127]: from itertools import zip_longest # needed for grouper
     ...: 
     ...: def grouper(iterable, n, fillvalue=None):
     ...:     "Collect data into fixed-length chunks or blocks"
     ...:     # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
     ...:     args = [iter(iterable)] * n
     ...:     return zip_longest(fillvalue=fillvalue, *args)
     ...:     
     ...: 

In [128]: by_fives = list(grouper(Types, 5))

In [130]: by_fives[1]
Out[130]: 
(['Which of the following is a purpose of the Amateur Radio Service as stated in the FCC rules and regulations?',
  ''],
 ['A. Providing personal radio communications for as many citizens as possible',
  ''],
 ['B. Providing communications for international non-profit organizations',
  ''],
 ['C. Advancing skills in the technical and communication phases of the radio art',
  ''],
 ['D. All of these choices are correct ', ''])

In [131]: by_fives[0]
Out[131]: 
(['SUBELEMENT T1 – FCC Rules, descriptions and definitions for the Amateur Radio Service, operator and station license responsibilities - [6 Exam Questions - 6 Groups]',
  ''],
 ['', ''],
 ['T1A - Amateur Radio Service: purpose and permissible use of the Amateur Radio Service; operator/primary station license grant; where FCC rules are codified; basis and purpose of FCC rules; meanings of basic terms used in FCC rules; interference; spectrum management',
  ''],
 ['', ''],
 ['T1A01 (C) [97.1]', ''])

In [133]: Types[0]
Out[133]: 
['SUBELEMENT T1 – FCC Rules, descriptions and definitions for the Amateur Radio Service, operator and station license responsibilities - [6 Exam Questions - 6 Groups]',
 '']

In [134]: del Types[0-2]

In [135]: Types[0]
Out[135]: 
['SUBELEMENT T1 – FCC Rules, descriptions and definitions for the Amateur Radio Service, operator and station license responsibilities - [6 Exam Questions - 6 Groups]',
 '']

In [136]: del Types[0]

In [137]: Types[0]
Out[137]: ['', '']

In [138]: del Types[0]

In [139]: Types[0]
Out[139]: 
['T1A - Amateur Radio Service: purpose and permissible use of the Amateur Radio Service; operator/primary station license grant; where FCC rules are codified; basis and purpose of FCC rules; meanings of basic terms used in FCC rules; interference; spectrum management',
 '']

In [140]: by_fives = list(grouper(Types, 5))

In [141]: by_fives[1]
Out[141]: 
(['B. Providing communications for international non-profit organizations',
  ''],
 ['C. Advancing skills in the technical and communication phases of the radio art',
  ''],
 ['D. All of these choices are correct ', ''],
 ['~~', ''],
 ['', ''])

In [142]: by_fives[0]
Out[142]: 
(['T1A - Amateur Radio Service: purpose and permissible use of the Amateur Radio Service; operator/primary station license grant; where FCC rules are codified; basis and purpose of FCC rules; meanings of basic terms used in FCC rules; interference; spectrum management',
  ''],
 ['', ''],
 ['T1A01 (C) [97.1]', ''],
 ['Which of the following is a purpose of the Amateur Radio Service as stated in the FCC rules and regulations?',
  ''],
 ['A. Providing personal radio communications for as many citizens as possible',
  ''])

In [143]:   



# Progress on 12/12

In [154]: f = open('/Users/james/repos/hamgame/ham_questions_groomed.txt','r')
     ...: readLines = f.readlines()
     ...: Types = [line.split("\n") for line in readLines]
     ...: 
 
In [159]: by_eights = list(grouper(Types, 8))

In [160]: by_eights[0]
Out[160]: 
(['~~', ''],
 ['', ''],
 ['T1A01 (C) [97.1]', ''],
 ['Which of the following is a purpose of the Amateur Radio Service as stated in the FCC rules and regulations?',
  ''],
 ['A. Providing personal radio communications for as many citizens as possible',
  ''],
 ['B. Providing communications for international non-profit organizations',
  ''],
 ['C. Advancing skills in the technical and communication phases of the radio art',
  ''],
 ['D. All of these choices are correct ', ''])

In [161]: by_eights[1]
Out[161]: 
(['~~', ''],
 ['', ''],
 ['T1A02 (C) [97.1]', ''],
 ['Which agency regulates and enforces the rules for the Amateur Radio Service in the United States?',
  ''],
 ['A. FEMA', ''],
 ['B. The ITU', ''],
 ['C. The FCC', ''],
 ['D. Homeland Security', ''])


In [168]: import re

In [169]: test = re.split(r'[()]',by_eights[1][2])
     ...: 
     ...: 
     ...: 
     ...: 
     ...: 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-169-13c5258aff6b> in <module>()
----> 1 test = re.split(r'[()]',by_eights[1][2])
      2 
      3 
      4 
      5 

/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/re.py in split(pattern, string, maxsplit, flags)
    201     and the remainder of the string is returned as the final element
    202     of the list.'"""'
    203     return _compile(pattern, flags).split(string, maxsplit)
    204 
    205 def findall(pattern, string, flags=0):

TypeError: expected string or bytes-like object



# Better progress: 12/12


f = open('/Users/james/repos/hamgame/ham_questions_groomed.txt','r')
data = f.read().splitlines()

by_eights[1][2]
'T1A02 (C) [97.1]'

by_eights = list(grouper(data, 8))

re.split(r'[()]',by_eights[1][2])[1]
'C'

#see defaultdict : https://stackoverflow.com/questions/960733/python-creating-a-dictionary-of-lists

for i in range(0,426):
    print(by_eights[i][1])                  
                                                                                     

# Read in questions to dictionary

bigdct={} 

for i in range(0,426):
    id=re.split(r'[ ()]',by_eights[i][2])[0]
    bigdct[id] = {}
    bigdct[id]['correct_ans']=re.split(r'[()]',by_eights[i][2])[1]
    bigdct[id]['question']=by_eights[i][3]
    bigdct[id]['ans_a']=by_eights[i][4]
    bigdct[id]['ans_b']=by_eights[i][5]
    bigdct[id]['ans_c']=by_eights[i][6]
    bigdct[id]['ans_d']=by_eights[i][7]
    
print(bigdct["T9A13"]["question"])

bigdct["T9A13"]


In [252]: bigdct['T9A13'].items()
Out[252]: dict_items([('question', 'Why are VHF or UHF mobile antennas often mounted in the center of the vehicle roof?'), ('ans_a', 'A. Roof mounts have the lowest possible SWR of any mounting configuration'), ('ans_d', 'D. Roof mounted antennas are always the easiest to install'), ('correct_ans', 'C'), ('ans_c', 'C. A roof mounted antenna normally provides the most uniform radiation pattern '), ('ans_b', 'B. Only roof mounting can guarantee a vertically polarized signal')])

In [253]: bigdct['T9A13'].keys()
Out[253]: dict_keys(['question', 'ans_a', 'ans_d', 'correct_ans', 'ans_c', 'ans_b'])

In [254]: bigdct['T9A13'].values()

#json testing

import json
test = json.dumps(bigdct)   
loaded_test=json.loads(test)

In [261]: loaded_test['T9B11']
Out[261]: 
{'ans_a': 'A. 50-ohm flexible coax',
 'ans_b': 'B. Multi-conductor unbalanced cable',
 'ans_c': 'C. Air-insulated hard line',
 'ans_d': 'D. 75-ohm flexible coax',
 'correct_ans': 'C',
 'question': 'Which of the following types of feed line has the lowest loss at VHF and UHF?'}

# Test looping through nested dict

 In [266]: for k,v in bigdct['T9A13'].items():
     ...:     print("{0}".format(v))
     ...:     
Why are VHF or UHF mobile antennas often mounted in the center of the vehicle roof?
A. Roof mounts have the lowest possible SWR of any mounting configuration
D. Roof mounted antennas are always the easiest to install
C
C. A roof mounted antenna normally provides the most uniform radiation pattern 
B. Only roof mounting can guarantee a vertically polarized signal

# 12/14
# function to display questions to Users

def present_question(chosen_question):
    """
    Present a question to the player
    """
    print(bigdct[chosen_question]['question'])
    print(bigdct[chosen_question]['ans_a'])
    print(bigdct[chosen_question]['ans_b'])
    print(bigdct[chosen_question]['ans_c'])
    print(bigdct[chosen_question]['ans_d'])
