import random

def  getChoice ():
    options =[" rock", "paper", "scissor"]
    player_choice = input("Enter a choice (rock,paper,scissor): ")
    computer_choice = random.choice(options) 
    choices = {
        "player": player_choice,
        "computer": computer_choice
    }
    return choices

def checker (computer , player):
    if player == computer:
        return "it's a tie"
    # Rock
    elif player == "rock" :
        if computer == "scissor":
            return "Rock smashes scissor!  You Won!"
        else:
            return "paper cover rock!  You lose!"

    elif player == "paper" :
        if computer == "rock":
            return "paper cover rock!  You Won!"
        else:
            return "scissor cut paper!  You lose!"
        
    elif player == "scissor" :
        if computer == "paper":
            return "scissor cut paper!  You Won!"
        else:
            return "Rock smashes scissor!  You lose!"
     

 
_response =  getChoice()
print(_response)
checkResult =checker(_response["computer"], _response["player"])
print(checkResult)

hello = "hi"
print(f' Iboytech is learning  {hello }')