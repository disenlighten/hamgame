#!/usr/bin/env python3

#module imports
import json
import random

#define variables
correct_count = 0
known_count = 0
wrong_ans={}
known_ans=[]
bigdct={}
valid_answers=['a', 'b', 'c', 'd']
my_guess = ""

#define prompt - 
prompt = "\n  > "


#load dictionary
with open('/Users/james/repos/hamgame/technician_questions.json') as json_data:
    bigdct=json.load(json_data)
json_data.close()

#load known_ans
#tbd 12/15

#define functions
def showme(chosen_question):
    """
    Get the correct answer immediately
    """
    print(bigdct[chosen_question]['correct_ans'])
    wrong_ans.update({chosen_question:"skipped"})
    return True

def present_question(chosen_question):
    """
    Present a question to the player
    """
    print(bigdct[chosen_question]['question'])
    print(bigdct[chosen_question]['ans_a'])
    print(bigdct[chosen_question]['ans_b'])
    print(bigdct[chosen_question]['ans_c'])
    print(bigdct[chosen_question]['ans_d'])

# Main loop
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
    elif my_guess == 'showme':
        showme(chosen_question)
    elif my_guess != 'quit':
        print("\n Answer must be a letter a, b, c, or d.")
    elif my_guess == 'quit':
            print("Goodbye! Keep studying, turkey legs!")
            my_guess=''
            wrong_ans={}
            break


# Notes: 12/15:
#Needed features: 
# * limit to 35 questions
# * score at the end
# * Make the help and "invalid answer" conditions return to the same question
# * Implement the count for correct answers