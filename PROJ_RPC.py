#Rock Paper Scissors 
from random import randint 
print ("Welcome to the game!")



var=("rock", "paper", "scissors")




c=1
while c>0:
    com=var[randint(0,2)]
    user=input("Enter your Move: ")   
    user=user.lower()
    if user==("exit"):
        break 

    while com==var[0]:
        if user==var[0]:
            print ("Computer: ", com.title())
            print ("It's a Draw")
        elif user==var[1]:
            print ("Computer: ", com.title())
            print ("You Win!")
        elif user==var[2]:
            print ("Computer: ", com.title())
            print ("Computer Wins!")
        else:
            print ("invalid input")    
            print ("____________________")
            print ("type 'exit' to QUIT")   
        break

    while com==var[1]:
        if user==var[1]:
            print ("Computer: ", com.title())
            print ("It's a Draw")
        elif user==var[2]:
            print ("Computer: ", com.title())
            print ("You Win!")
        elif user==var[0]:
            print ("Computer: ", com.title())
            print ("Computer Wins!")
        else:
            print ("invalid input") 
            print ("____________________")
            print ("type 'exit' to QUIT")   
        
        break

    while com==var[2]:
        if user==var[2]:
            print ("Computer: ", com.title())
            print ("It's a Draw")
        elif user==var[0]:
            print ("Computer: ", com.title())
            print ("You Win!")
        elif user==var[1]:
            print ("Computer: ", com.title())
            print ("Computer Wins!")
        else:
            print ("invalid input")    
            print ("____________________")
            print ("type 'exit' to QUIT")   
        
        break            














