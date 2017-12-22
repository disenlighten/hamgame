#!/usr/bin/env python3

#module imports
import json
import random

#define variables
correct_count = 0
known_count = 0
wrong_ans={}
known_ans={}
quiz_used=[]
bigdct={}
valid_answers=['a', 'b', 'c', 'd']
my_guess = ""

#define prompt - 
prompt = "\n  > "

#define helptext
helptext = "\n Enter the letter of your answer."
helptext += "\n Enter 'showme' to see the answer now. "
helptext += "\n Enter 'quit' to end the program."

#load dictionary
with open('./technician_questions.json') as json_data:
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

def check_input(current_guess):
    """
    Checks input and handles exceptions
    """
    if current_guess in valid_answers:
        return True
    if current_guess == 'showme':
        showme(chosen_question)
        return True
    if current_guess == 'help':
        print(helptext)
        return True            
    if len(current_guess) > 1 and current_guess != "quit":
        print("You may only guess 1 letter at a time, please.")
        return True
    if not current_guess in valid_answers:
        print("Valid answer are a, b, c, d.")
        return True
    #else:
        
     #   return False

def present_question(chosen_question):
    """
    Present a question to the player
    """
    print(bigdct[chosen_question]['question'])
    print(bigdct[chosen_question]['ans_a'])
    print(bigdct[chosen_question]['ans_b'])
    print(bigdct[chosen_question]['ans_c'])
    print(bigdct[chosen_question]['ans_d'])

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

# Main loop
total_question_count=0
while total_question_count<34 and my_guess != 'quit':
    chosen_question=random.choice(list(bigdct.keys()))
    if chosen_question not in quiz_used:
        total_question_count+=1
        present_question(chosen_question)
        my_guess = (input(prompt)).lower()
        while my_guess != 'quit':
            if check_input(my_guess):
                if my_guess == bigdct[chosen_question]['correct_ans']:
                    correct_count +=1
                    known_ans.update({chosen_question:known_count}) 
                    known_ans[chosen_question] +=1
                    quiz_used.append(chosen_question)
                    break       
                else:
                    quiz_used.append(chosen_question)
                    wrong_ans.update({chosen_question:my_guess})
                    break
    
        
            elif my_guess == 'quit':
                    print("\n Goodbye! Keep studying, turkey legs!")
                    present_results(correct_count,wrong_ans)
                    my_guess=''
                    wrong_ans={}
                    quiz_used=[]
                    break
present_results(correct_count,wrong_ans)
my_guess=''
wrong_ans={}
quiz_used=[]
