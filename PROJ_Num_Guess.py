#GUESSING GAME

from random import randint

def random():
    num=randint(1,99)

    print  ("Guess a two digit number!")

    guess=0
    c=0
    while num!=guess:
        guess=int(input("Enter your guess: "))
        
        if guess>num:
            c=c+1
            print("Try guessing lower")   
        elif guess<num:
            c=c+1
            print("Guess higher")    
        else:
            c=c+1
            print ("You guessed it ")
            print (f"Took you {c} tries.")


random()
