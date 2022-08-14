#create a dictionary of questions and answers 
solutions = {"what does cpu stands for ?" : 'central processing unit' ,
             "what does ram stands for ?" : 'random access memory' ,
             "which company uses ios as its mobile operating system ?" : 'Apple' ,
             "which is the keyword for creating a table in a database ?" : 'CREATE' ,
             "which part of the computer stores the loading program for operating system into the ram ?" : 'EEPROM' ,
             "what was the name of the first electronic computer ?" : 'ENIAC' ,
             "how many bits are there in a byte ?" : '8' ,
              "who wrote the first computer algorithm ever ?" : 'Lady Ada LoveLace' ,
              "which is the most common part of the internet ?" : 'Surface web' ,
              "what does psu stands for ?" : 'Power Supply Unit'
             }


scores = 0 
def check_answer(question , user_input ) :
    if(solutions[question.lower()].lower() == user_input.lower()) :
        print("You got this correct !")
        global scores
        scores += 1
    else :
         print("OOPS ! you got this wrong ")


player_permission = input("Do you wish to start the game ? ")

if(player_permission.lower() != 'yes') :
    #quit the game
    quit()
else :

    question1 = "What does CPU stands for ?"
    answer1 = input(question1 + "\t")
    check_answer(question1, answer1)
    
    question2 = "What does RAM stands for ?"
    answer2 = input(question2 + "\t")
    check_answer(question2 , answer2)

    question3 = "What does PSU stands for ?"
    answer3 = input(question3 + '\t')
    check_answer(question3 , answer3)

    question4 = "Which company uses IOS as its mobile operating system ?"
    answer4 = input(question4 + '\t') 
    check_answer(question4 , answer4)

    question5 = "Which is the keyword for creating a table in a database ?"
    answer5 = input(question5 + '\t')
    check_answer(question5 , answer5)

    question6 = "Which part of the computer stores the loading program for operating system into the RAM ?"
    answer6 = input(question6 + '\t')
    check_answer(question6 , answer6)
    
    question7 = "What was the name of the first electronic computer ?"
    answer7 = input(question7 + '\t')
    check_answer(question7 , answer7)

    question8 = "How many bits are there in a byte ?"
    answer8 = input(question8  + '\t')
    check_answer(question8 , answer8) 

    question9 = "Who wrote the first computer algorithm ever ?"
    answer9 = input(question9  + '\t')
    check_answer(question9 , answer9)

    question10 = "Which is the most common part of the internet ?"
    answer10 = input(question10 + '\t')
    check_answer(question10 , answer10)

    print("\nYour total Score is : {}".format(scores))
    print("Thank you visit again !")

    

