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
    bigdct[id]['correct_ans']=(re.split(r'[()]',by_eights[i][2])[1]).lower()
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

#import needed modules
import random

#Define varaibles
correct_count = 0
known_count = 0
wrong_ans={}
known_ans={}
valid_answers=['a', 'b', 'c', 'd']
my_guess = ""

#define prompt - 
prompt = "\n  > "


helptext = "\n Enter the letter of your answer."
helptext += "\n Enter 'showme' to see the answer now. "
helptest += "\n Enter 'quit' to end the program."

#initialize my_guess variable


def present_question(chosen_question):
    """
    Present a question to the player
    """
    print(bigdct[chosen_question]['question'])
    print(bigdct[chosen_question]['ans_a'])
    print(bigdct[chosen_question]['ans_b'])
    print(bigdct[chosen_question]['ans_c'])
    print(bigdct[chosen_question]['ans_d'])


present_question(chosen_question)
my_guess = (input(prompt)).lower()

# Notes on adding color to python
#http://ozzmaker.com/add-colour-to-text-in-python/


# Testing the valid_answers array
In [287]: my_guess in valid_answers
Out[287]: True

# set the answer letters to lowercase 
    bigdct[id]['correct_ans']=(re.split(r'[()]',by_eights[i][2])[1]).lower()

In [294]: print(bigdct["T9A13"]["correct_ans"])
c

# Testing truth condition
In [315]: my_guess='c'

In [316]: my_guess == bigdct[chosen_question]['correct_ans']
Out[316]: True

#chosen_question=random.choice(bigdct[id]['question'])


# First Test loop - confirmed sort of works!
while my_guess != 'quit':
    chosen_question=random.choice(list(bigdct.keys()))
    present_question(chosen_question)
    my_guess = (input(prompt)).lower()
    if my_guess in valid_answers:
        if my_guess == bigdct[chosen_question]['correct_ans']:
            correct_count +=1
            known_ans.append(chosen_question)   
        else:
            wrong_ans.update({chosen_question:my_guess})  
    elif my_guess != 'quit':
        print("\n Answer must be a letter a, b, c, or d.")
    elif my_guess == 'quit':
            print("Goodbye! Keep studying, turkey legs!")
            break


#12/15
#json testing part 2
#main terminal 

# dump the dictonary to json
In [356]: import json
     ...: test = json.dumps(bigdct)

# open a new file for writing
In [358]: f = open('/Users/james/repos/hamgame/technician_questions.json', 'w')

#write out json to the file
In [359]: f.write(test)


#2nd terminal
In [1]: import json

#define the dictionary
In [2]: bigdct = {}

#repopulate the dictionary
In [3]: with open('/Users/james/repos/hamgame/technician_questions.json') as json_data:
   ...:     bigdct=json.load(json_data)
   ...: 

#close the open file 
In [6]: json_data.close()

#validate
In [7]: print(bigdct["T9A13"]["question"])
Why are VHF or UHF mobile antennas often mounted in the center of the vehicle roof?

###

#make a function to show the answer

def showme(chosen_question):
    """
    Get the correct answer immediately
    """
    print(bigdct[chosen_question]['correct_ans'])
    wrong_ans.update({chosen_question:"skipped"})
    return True


# Second Test loop - testing showme - confirmed, works!
while my_guess != 'quit':
    chosen_question=random.choice(list(bigdct.keys()))
    present_question(chosen_question)
    my_guess = (input(prompt)).lower()
    if my_guess in valid_answers:
        if my_guess == bigdct[chosen_question]['correct_ans']:
            correct_count +=1
            known_ans.update({chosen_question:known_count++})   
        else:
            wrong_ans.update({chosen_question:my_guess})  
    elif my_guess == 'showme':
        showme(chosen_question)
# Help not working
#    elif my_guess == 'help':
#        my_guess = (input(helptext)).lower()
    elif my_guess != 'quit':
        #Has the same problem as help - presents a new question afterward...
        print("\n Answer must be a letter a, b, c, or d.")
    elif my_guess == 'quit':
            print("Goodbye! Keep studying, turkey legs!")
            my_guess=''
            wrong_ans={}
            break


#12/18 - more attempted refinements to main loop


helptext = "\n Enter the letter of your answer."
helptext += "\n Enter 'showme' to see the answer now. "
helptext += "\n Enter 'quit' to end the program."

def check_input(current_guess):
    """
    Checks input and handles exceptions
    """
    if current_guess in valid_answers:
        return True
    if my_guess == 'showme':
        showme(chosen_question)
        return True
    if current_guess == 'help':
        print(helptext)
        return True            
    if len(current_guess) > 1 and current_guess != "quit":
        print("You may only guess 1 letter at a time, please.")
        return False
    else:
        return False

total_question_count=0
while total_question_count<34 and my_guess != 'quit':
    chosen_question=random.choice(list(bigdct.keys()))
    total_question_count+=1
    present_question(chosen_question)
    my_guess = (input(prompt)).lower()
    while my_guess != 'quit':
        if check_input(my_guess):
        #if my_guess in valid_answers:
              if my_guess == bigdct[chosen_question]['correct_ans']:
                  correct_count +=1
                  known_ans.update({chosen_question:known_count}) 
                  known_ans[chosen_question] +=1
                  break 
              else:
                  wrong_ans.update({chosen_question:my_guess})
                  break  
        elif my_guess == 'quit':
            print("Goodbye! Keep studying, turkey legs!")
            my_guess=''
            wrong_ans={}

            break

#problems - quit still does not work
#total question count not getting incremented
#could use a counter to stay on same question?

#new problems - 12/19
#An invalid answer dumps you into a loop where nothing happens
#help is caught by the condition of alerting on multiple letters
# After you choose multiple letters, it _still_ gives you a new question

def present_results(score, wrong_answers):
    """
    Presents the score and wrong/correct answers to player
    """
    final_score = (score/35)*100
    print("Your final score is: " + (str(round(final_score))))
    
    if final_score > 80: 
        print("You passed!")
    else:
        print("You failed.")

    for k,v in wrong_answers.items():
        print("Question ID: " +  k)
        print(bigdct[k]['question'])
        print(bigdct[k]['ans_a'])
        print(bigdct[k]['ans_b'])
        print(bigdct[k]['ans_c'])
        print(bigdct[k]['ans_d'])
        print("Your answer was: " + v) 
        print("The correct answer is: " + bigdct[k]['correct_ans'])


# Test code for using the wrong_ans dict
In [109]: for k,v in wrong_ans.items():
     ...:     print("Your answer was:" +  k)
     ...:     print("The question id was" + v)

In [117]: present_results(correct_count,wrong_ans)
Your final score is: 63
You failed.
Question ID: T6B10
What are the three electrodes of a PNP or NPN transistor?
A. Emitter, base, and collector
B. Source, gate, and drain
C. Cathode, grid, and plate
D. Cathode, drift cavity, and collector
Your answer was: db
The correct answer is: a
Question ID: T1F11
To which foreign stations do the FCC rules authorize the transmission of non-emergency third party communications?
A. Any station whose government permits such communications
B. Those in ITU Region 2 only
C. Those in ITU Regions 2 and 3 only
D. Those in ITU Region 3 only
Your answer was: help
The correct answer is: a
Question ID: T5D07
What is the current flow in a circuit with an applied voltage of 120 volts and a resistance of 80 ohms?
A. 9600 amperes
B. 200 amperes
C. 0.667 amperes
D. 1.5 amperes
Your answer was: showme
The correct answer is: d
Question ID: T7D02
What is the correct way to connect a voltmeter to a circuit?
A. In series with the circuit
B. In parallel with the circuit
C. In quadrature with the circuit
D. In phase with the circuit
Your answer was: showme
The correct answer is: b
Question ID: T0B10
Which of the following is true concerning grounding conductors used for lightning protection?
A. Only non-insulated wire must be used
B. Wires must be carefully routed with precise right-angle bends
C. Sharp bends must be avoided
D. Common grounds must be avoided
Your answer was: d
The correct answer is: c


***

#Open the correct answers file
with open('./correct_answers.json') as json_data:
    kwown_ans=json.load(json_data)
json_data.close()

#Write to the correct answers file 
f = open('./correct_answers.json', 'w')
  
f.write(test2)

f.close()

***

# bash commands to turn wrong answer corrections into a study guide
grep 'Question ID' hamquiz_2017122* | awk -F"[T]" '{ print $2 }' | sed s/^/T/g | sort -u > study_question_id.txt
for x in $(cat study_question_id.txt); do grep -A7 $x ~/repos/hamgame/ham_questions_groomed.txt ; done > study_guide.txt

### Notes on colored text: 
# Python 3
print("\x1b[1;“32m”;40m Bright Green  \n")
# Python 2.7
print("\033[1;31;40m Bright Red  \n")

#Return the terminal to normal color
print("\x1b[0m")

