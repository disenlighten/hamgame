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




In [113]: for e in Types[1:5:]:
     ...:     print e
  File "<ipython-input-113-a0c7481d9560>", line 2
    print e
          ^
SyntaxError: Missing parentheses in call to 'print'


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

In [118]: from itertools import izip_longest # needed for grouper
     ...: 
     ...: def grouper(iterable, n, fillvalue=None):
     ...:     "Collect data into fixed-length chunks or blocks"
     ...:     # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
     ...:     args = [iter(iterable)] * n
     ...:     return izip_longest(fillvalue=fillvalue, *args)
     ...: 
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-118-87c2e792e7da> in <module>()
----> 1 from itertools import izip_longest # needed for grouper
      2 
      3 def grouper(iterable, n, fillvalue=None):
      4     "Collect data into fixed-length chunks or blocks"
      5     # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx

ImportError: cannot import name 'izip_longest'

In [119]: from intertools import izip_longest
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-119-6cf9d48cb5cc> in <module>()
----> 1 from intertools import izip_longest

ImportError: No module named 'intertools'

In [120]: from itertools import izip_longest
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-120-61e5597c5f71> in <module>()
----> 1 from itertools import izip_longest

ImportError: cannot import name 'izip_longest'

In [121]: from itertools import izip
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-121-e1e6597ef5d6> in <module>()
----> 1 from itertools import izip

ImportError: cannot import name 'izip'

In [122]: from itertools import *

In [123]: izip
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-123-461917860708> in <module>()
----> 1 izip

NameError: name 'izip' is not defined

In [124]: from more-itertools install izip_longest
  File "<ipython-input-124-7c9d576cb584>", line 1
    from more-itertools install izip_longest
             ^
SyntaxError: invalid syntax


In [125]: from more_itertools install izip_longest
  File "<ipython-input-125-1b0c695d0797>", line 1
    from more_itertools install izip_longest
                              ^
SyntaxError: invalid syntax


In [126]: from more_itertools import izip_longest
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-126-1325c1a0fe99> in <module>()
----> 1 from more_itertools import izip_longest

ImportError: cannot import name 'izip_longest'

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

In [132]: Types(pop)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-132-a9231507a6ad> in <module>()
----> 1 Types(pop)

NameError: name 'pop' is not defined

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
                    
                                                                                     
