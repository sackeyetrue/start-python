# First Python Project
# A Rock Paper Sccisors Game 
import random

print("ZEKE: ROCK PAPER SCISSORS GAME")


# Gets the Chioces of Computer and User
def getchoices():
    playerChoice = input("Enter Choice (Rock,Paper,Scissors): ")
    option = ["Rock","Paper","Scissors"]
    computerChoice = random.choice(option)
    choices = {"player":playerChoice,"computer":computerChoice}
    return choices

# Get who Wins the Game
def getWin(player,computer):
    #Print Both Choices 
    print(f"You Chose: {player},Computer Chose:{computer}")
    
    if player == computer:
        return "It's a tie"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock Smaches Scissors, You Win!!!"
        else :
            return "Paper Covers Rock, You Lose!!!"
        
    elif player == "Paper":
        if computer == "Rock":
            return "Paper Covers Rock, You Win!!!"
        else :
            return "Scissors Cuts Paper, You Lose!!!"
        
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors Cuts Paper, You Win!!!"
        else :
            return "Rock Smashes Scissors, You Lose!!!"
    
choices = getchoices()
results = getWin(choices["player"],choices["computer"])
print(results)