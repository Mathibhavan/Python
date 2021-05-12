from random import random
from Tools.scripts.dutree import display
print("Welcome to Hang man game")
name=input("Enter your name")
print("Hello "+name+ " Best of Luck")
print("Let's start the game")
def main():
    global play_game
    global word
    global display
    global count
    global length
    global already_guessed
    guess_word=["Platinum","candy","superficial","optimistic","blueberry","gratitude"]
    word=random.choice(guess_word)
    count=0
    length=len(word)
    display='_'*length
    already_guessed=[]
    play_game=""

def play_game():
    global play_game
    print("Do you want to play  ? yes/no")
    if "yes":
        main()
    else:
        print("Thanks for playing")
        exit()
    main()
 
      