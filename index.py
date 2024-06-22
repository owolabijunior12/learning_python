import random

def  getChoice ():
    options =[" rock", "paper", "scissor"]
    player_choice = input("Enter a choice (rock,paper,scissor: ")
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
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissor!  You Won!"
    # Scissor
    elif player =="scissor" and computer == "paper":
       return "Player Won"
   
    # paper
    elif player =="scissor" and computer == "":
       return "Player Won"
 
   
   
 
# response =  getChoice()
hello = "hi"
print(f' Iboytech is learning  {hello }')