# MAIN 

import os
import question_model
import quizgamebrain

myQuestion = question_model.question()

os.system('cls')

correct_answers = 0
incorrect_answers = 0

while True:
    
    # SET QUESTION
    myQuestion.setQuestion() 
    question = myQuestion.getQuestion()
    answer = myQuestion.getAnswer()

    # PUT QUESTION ON THE BRAIN
    myBrain = quizgamebrain.quizBrain(question,answer)

    # GET ANSWERS
    print("\nQuestion: {}".format(question))
    
    while True:
        input_answer= str(input("Type your answer (True/False): "))
        if (input_answer == "True"):
            break
        elif (input_answer == "False"):
            break
        else:
            print("Try your answer again...")
    
    myBrain.setChoosenAnswer(input_answer)

    evaluation = myBrain.evaluateAnswer()

    if evaluation == True:
        print("Your answer is correct!")
        correct_answers += 1
    elif evaluation == False:
        print("Your answer is wrong")
        incorrect_answers +=1

    print("\nCorrect answers: {}".format(correct_answers))
    print("Wrong answers: {}".format(incorrect_answers))

    if incorrect_answers > 2:
        print("\nGame over: YOU LOSE!")
        break
    elif (correct_answers >= 5):
        print("\nGame over: YOU WIN!")
        break
    else:
        pass
