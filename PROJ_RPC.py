#Rock Paper Scissors 
from random import randint 
print ("Welcome to the game!")



var=("Rock", "Paper", "Scissors")
com=var[randint(0,2)]

c=1
while c>0:
    user=input("Enter your Move: ")   
    if user==("exit"):
        break 

    while com==var[0]:
        if user==var[0]:
            print ("Computer: ", com)
            print ("It's a Draw")
        elif user==var[1]:
            print ("Computer: ", com)
            print ("You Win!")
        elif user==var[2]:
            print ("Computer: ", com)
            print ("Computer Wins!")
        else:
            print ("invalid input")    
        break

    while com==var[1]:
        if user==var[1]:
            print ("Computer: ", com)
            print ("It's a Draw")
        elif user==var[2]:
            print ("Computer: ", com)
            print ("You Win!")
        elif user==var[0]:
            print ("Computer: ", com)
            print ("Computer Wins!")
        else:
            print ("invalid input") 
            print ("____________________")
            print ("type 'exit' to QUIT")   
        break

    while com==var[2]:
        if user==var[2]:
            print ("Computer: ", com)
            print ("It's a Draw")
        elif user==var[0]:
            print ("Computer: ", com)
            print ("You Win!")
        elif user==var[1]:
            print ("Computer: ", com)
            print ("Computer Wins!")
        else:
            print ("invalid input")    
        break            














