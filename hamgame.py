#!/usr/bin/env python3

#module imports
import json
import random
import webbrowser
import os

#define variables
correct_count = 0
known_count = 0
wrong_ans={}
known_ans={}
quiz_used=[]
bigdct={}
valid_answers=('a', 'b', 'c', 'd')
figure_questions=('G7A11', 'G7A12')
my_guess = ""
exit_game = ""
question_in_progress = ""

#define prompt - 
prompt = "\n  > "

#define helptext
helptext = "\n Enter the letter of your answer."
helptext += "\n Enter 'showme' to see the answer now. "
helptext += "\n Enter 'quit' to end the program."

#define functions
#def open_file(path_to_graphic):
#  webbrowser.open('file://' + (os.path.join(, path_to_graphic)))

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
    elif current_guess == 'showme':
        showme(chosen_question)
    elif current_guess == 'help':
        print(helptext)        
    elif len(current_guess) > 1 and current_guess != "quit":
        print("You may only guess 1 letter at a time, please.")
    elif current_guess == "quit":
        global exit_game
        exit_game = True
        return exit_game
    else:
        print("Valid answer are a, b, c, d.")
        global question_in_progress
        question_in_progress = True

def present_question(chosen_question,figure_questions):
    """
    Present a question to the player
    """
    print(chosen_question)
    print(bigdct[chosen_question]['question'])
    print(bigdct[chosen_question]['ans_a'])
    print(bigdct[chosen_question]['ans_b'])
    print(bigdct[chosen_question]['ans_c'])
    print(bigdct[chosen_question]['ans_d'])

#    if test_type == "2":
#       if chosen_question in figure_questions:
#            open_file('./images/general/figure_g7-1.png')

def present_results(score, wrong_answers):
    """
    Presents the score and wrong/correct answers to player
    """
    final_score = (score/35)*100
    print("Your final score is: " + (str(round(final_score))))
    
    if final_score >= 80: 
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

def load_data(test_type):
  """
  Load the question set for the chosen test
  """
  global bigdct
  if test_type == "1":
      with open('./technician_questions.json') as tech_json_data:
        bigdct=json.load(tech_json_data)
        tech_json_data.close()
  elif test_type == "2":
      with open('./general_questions.json') as gen_json_data:
        bigdct=json.load(gen_json_data)
        gen_json_data.close()
  elif test_type == "3":
      with open('./extra_questions.json') as ext_json_data:
        bigdct=json.load(ext_json_data)
        ext_json_data.close()
  # needs to be an exception
  else:
       print("Invalid selection.")

def get_test_question_count(test_type):
    if (test_type == "1" or test_type == "2"):
        question_count = 34
    elif test_type == "3":
        question_count = 66
    return question_count

# Main loop
#test_type = ""
print("\nChoose a test:")
print("\nEnter 1 for Technician Class")
print("\nEnter 2 for General Class")
print("\nEnter 3 for Extra Class")
test_type = (input(prompt)).lower()
load_data(test_type)
total_question_count=0
test_question_count = get_test_question_count(test_type)

while total_question_count<test_question_count and not exit_game:
        if not question_in_progress:
            chosen_question=random.choice(list(bigdct.keys()))
            if chosen_question not in quiz_used:
                present_question(chosen_question, figure_questions)
                my_guess = (input(prompt)).lower()
                if check_input(my_guess):
                    if my_guess == bigdct[chosen_question]['correct_ans']:
                        total_question_count+=1
                        correct_count +=1
                        known_ans.update({chosen_question:known_count})
                        known_ans[chosen_question] +=1
                        quiz_used.append(chosen_question)
                        print("\x1b[1;32;40m ----------------  \n")
                        print("\x1b[0m")
                    elif exit_game:
                        print("\n Goodbye! Keep studying, turkey legs!")
                        present_results(correct_count,wrong_ans)
                        my_guess=''
                        wrong_ans={}
                        quiz_used=[]
                        break
                    else:
                        total_question_count+=1
                        quiz_used.append(chosen_question)
                        wrong_ans.update({chosen_question:my_guess})
                        print("\x1b[1;31;40m ----------------  \n")
                        print("\x1b[0m")
present_results(correct_count,wrong_ans)
my_guess=''
wrong_ans={}
quiz_used=[]
