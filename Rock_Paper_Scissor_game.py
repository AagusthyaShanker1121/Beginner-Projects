from random import randint as ri

user_score = 0 
computer_score = 0

moves = ["rock" , "paper" , "scissor"]

want_rounds = input("Do you wish to play with rounds then type \"Yes\" otherwise type \"No\" \n\n\t\t")

# -----------------------------------------------------------------------------------------------------


if want_rounds.lower() == "yes" : 

    # Game with number of rounds 
    #Validating the input


    rounds = input("Enter the number of rounds you want to play :\t")
    plays = input("Enter the number of plays per round : \n")

    while rounds.isdigit() == False and plays.isdigit() == False :
        temp = input("Rounds should be a numeric value (more than or equal to 1) , Enter here :\t")
        temp2 = input("Plays should be a numeric value (more than or equal to 1) , Enter here :\t")
        if temp.isdigit() and temp2.isdigit():
           (rounds , plays) = (temp , temp2)
        else :
            continue

    rounds = int(rounds)
    plays = int(plays)

    while rounds <= 0 and plays <= 0 :
        temp = input("Rounds should be more than or equal to 1 , Enter here :\t")
        temp2 = input("Plays should be more than or equal to 1 , Enter here :\t")

        (rounds , plays) = (temp , temp2)

    
    rounds = rounds * plays

    while rounds >= 1 :
        user_input = input("Type Rock / Paper / Scissor / q for Quit the game :\n").lower()
        if (user_input == 'q') :
            break

        elif (user_input not in moves) :
            continue 

        else :
            random_number = ri(0 , 2)
            computer_input = moves[random_number]
            print(f"Computer chose {computer_input}")

            #check who won
            if (computer_input , user_input) == ("rock" , "paper") :
                user_score += 1 
            elif (computer_input , user_input) == ("paper" , "rock") :
                computer_score += 1 
            elif (computer_input , user_input) == ("scissor" , "paper") :
                computer_score += 1 
            elif (computer_input , user_input) == ("paper" , "scissor") :
                user_score += 1 
            elif (computer_input , user_input) == ("rock" , "scissor" ) :
                computer_score += 1
            elif (computer_input , user_input) == ("scissor" , "rock") :
                user_score += 1 
            else :
                pass

        rounds -= 1

# -----------------------------------------------------------------------------------------------------

elif want_rounds.lower() == "no" :

    #Game without the number of rounds


    while True :
        user_input = input("Type Rock / Paper / Scissor / q for Quit the game :\n").lower()

        if (user_input == 'q') :
            break
        elif user_input not in moves :
            continue
        else :
            random_number = ri(0 , 2)
            computer_input = moves[random_number]
            print(f"Computer chose {computer_input}")

            #check who won
            if (computer_input , user_input) == ("rock" , "paper") :
                user_score += 1 
            elif (computer_input , user_input) == ("paper" , "rock") :
                computer_score += 1 
            elif (computer_input , user_input) == ("scissor" , "paper") :
                computer_score += 1 
            elif (computer_input , user_input) == ("paper" , "scissor") :
                user_score += 1 
            elif (computer_input , user_input) == ("rock" , "scissor" ) :
                computer_score += 1
            elif (computer_input , user_input) == ("scissor" , "rock") :
                user_score += 1 
            else :
                pass

# -----------------------------------------------------------------------------------------------------


else :
    print("Type only yes or no , next time ")
    quit()
     
   
print(f"Your Score : {user_score}\nComputer's Score : {computer_score}")
if computer_score > user_score :
    print("You Lose ! ")
elif user_score > computer_score :
    print("You Won ! ")
else :
    print("Its a draw ! ") 

print("Thank you playing , visit again ") 

