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

# Test of for/in 
with open("/Users/james/Downloads/2014-2018 Tech Pool.txt") as f:
    for row in f: 
        if "~" in f:    
            print(f)  