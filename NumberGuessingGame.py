import random

def validate_integer(user_input) :
    if (user_input.isdigit()) :
        return True 
    else :
        return False



top_of_range = input("Enter number of your choice :\t")

if(validate_integer(top_of_range)) :
    top_of_range = int(top_of_range)
    if (top_of_range <= 0) :
        print("Enter a number larger than 0 next time ... ")
        quit()
else :
    print("Enter a number next time .... ") 
    quit()

random_number = random.randint(1 , top_of_range)

guesses = 0

while True :
    #ask user to enter his/her guess
    
    user_guess = input("Enter your guess :\t")

    #validating all the constraints on the guess
    if(validate_integer(user_guess)) :
        user_guess = int(user_guess)
        if (user_guess <= 0) :
            print("Enter a number greater than or equal to 1 ")
            continue
        elif (user_guess > top_of_range) :
            print("Enter a number lesser than or equal to the top range ") 
            continue
    else :
        print("Enter a number next time ...")
        continue


    guesses += 1 
    if (user_guess == random_number) :
        print("You guessed it right ")
        break 
    elif(user_guess > random_number) :
        print("Your guess is larger than the actual ")
    else :
        print("You guess is smaller than the actual ") 


plurality = ''
if (guesses == 1) :
    plurality = "guess"
else :
    plurality = "guesses"


print("\n\nYou took" , guesses , plurality)
print("Thanks for playing , visit again ! ")