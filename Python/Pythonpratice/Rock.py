def playagain():
    again=input("Want to continue  ?? yes/no")
    if again=="yes":
        playgame()
    else:
        print("Quite game")
        
def playgame():
    userchoice=input("Enter user choice")
    opponentchoice=input("Enter opponent choice")
    if userchoice==opponentchoice:
        print("Its a tie")
        playagain()
    elif userchoice=="rock" and opponentchoice=="paper":
        print("opponent won")
        playagain()
    elif userchoice=="rock" and opponentchoice=="scissor":
        print("user won")
        playagain()
    elif userchoice=="paper" and opponentchoice=="scissor":
        print("opponent won")
        playagain()
    elif userchoice=="paper" and opponentchoice=="rock":  
        print("user won")
        playagain()
    elif userchoice=="scissor" and opponentchoice=="rock":
        print("opponent won")
        playagain()
    else:
        print("user won")
        playagain()
    playgame() 
playgame()      
    