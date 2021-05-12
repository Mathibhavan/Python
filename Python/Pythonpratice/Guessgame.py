import random
attempt_list=[]
def score():
    if len(attempt_list)<=0:
        print("Currently no high score")
    else:
        print("The current score is {} attempts".format(min(attempt_list)))
def startgame():
    attempt=0   
    random_num=random.randint(1,10)
    name=input("Enter the player name")
    print("Welcome {} to the guess game".format(name))
    play=input("Want to play?? game Enter yes/no")
    if play=="no":
        print("Quite game")
    else:
        
        guess_num=int(input("Guess a number between 1 to 10"))
        if (guess_num<1) or (guess_num>10):
            print("Please enter the number in range") 
        elif guess_num==random_num:
            print("you have won in first attempt")   
            attempt+=1 
            attempt_list.append(attempt)
            print("It took you {} attempts".format(attempt_list))
        elif int(guess_num) > random_num:
            print("it is higher")
            attempt+=1
        elif int(guess_num) < random_num:
            print("it is lower")
            attempt+=1
startgame()
score()
