from random import *
import time
import math
i = 1
q = 1
speed = 0
y = True
long = 10
medium = 3
fast = 1
super = 0.1



#====================================================================================================================
while True:
    try:
        score = int(input("What is the max score? "))
        break  # Break out of the loop if the input was successfully converted to an integer
    except ValueError:
        print("Please enter a valid integer for the max score.")


while True:
    try:
        Amount_of_questions = int(input("How many questions? "))
        break  # Break out of the loop if the input was successfully converted to an integer
    except ValueError:
        print("Please enter a valid integer for the number of questions.")

if Amount_of_questions == 0:
    quit
while True:
    try:
        if Amount_of_questions == 1:
            cooldown = 0.1
        else:
            cooldown = float(input("Insert the cooldown time: "))
        break
    except ValueError:
        print("Please enter a valid integer for the cooldown time.")
#=========================================================================================================================

if Amount_of_questions == 1:
    intro = "Answer "+str(Amount_of_questions)+" question!"
else:
    intro = "Answer "+str(Amount_of_questions)+" questions!"
print(intro)
print("Are you ready?")

for countdown in range(3, 0, -1):
    print(countdown)
    time.sleep(1)  # Wait for 3 second

print("Go!")  # Indicate the start of the quiz
start_time = time.time()
for q in range(Amount_of_questions):

    one = randrange(1,10)
    two = randrange(1,10)
    print("\n")
    printt = "Question: " + str(i)
    print(printt)
    print("\n")
    X = str(one)+"x"+str(two)+": "
    while True:  # Keep asking until a valid integer is entered
        try:
            x = int(input(X))
            break  # Exit the loop if input is successfully converted to an integer
        except ValueError:
            print("Please insert a number")
            print("\n")
    #print(type(x))
    if x == one*two:
        print("Correct!")
        score
    elif x != one*two:
        print("Incorrect :(")
        minus = score/Amount_of_questions
        score -= minus
        print("the answer was:",one*two)
    #elif x == "quit" or x == "escape":
        #sys.quit

    time.sleep(cooldown)
    i += 1
print("\n")
end_time = time.time()
final_score = "Final Score: "+str(round(score)) + "%"
final_time = "You took "+str(round(end_time - start_time))+" seconds."
print(final_score)
if final_time == "You took 1 seconds.":
    final_time2 = "You took "+str(round(end_time - start_time))+" second."
    print(final_time2)
else:
    print(final_time)