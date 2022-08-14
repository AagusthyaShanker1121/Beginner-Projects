from random import shuffle 

game_list = [' ' , 'o' , ' ']
def shuffle_list(game_list) :
    shuffle(game_list)
    return game_list

def check_ball(game_list , user_input) :
    shuffle_list(game_list)
    if(game_list[user_input] == 'o') :
        return "You Won"
    else :
        for i in range(len(game_list)) :
            if (game_list[i] == 'o') :
                return (f"You Lose , The ball was in cup {i + 1}")

user_input = int(input("Guess the cup the ball could be in : ")) - 1 

while (user_input > 3 or user_input < 1) :
    re_input = int(input("Enter numbers only between 1 to 3 : "))
    user_input = re_input 


check_ball(game_list , user_input)