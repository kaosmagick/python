import random

def game():

    user=""
    while user!="q":
        com=random.choice(["r","p","s"])
        user=input("Enter your choice:").lower()
        if rules(user,com):
            print ("You Won")
        elif rules (com,user):
            print ("You lose")
        elif draw(user,com):
            print ("It's a draw")
        elif quit(user):
            print ("Thanks for playing")   
        else:
            print ("Invalid Input")


def rules(a,b):
#Rock beats Scissors
#Scissors beat Paper
#Paper beats Rock

    if (a=="r" and b=="s") or (a=="s" and b=="p") or (a=="p" and b=="r"):
        return True
    
def draw(a,b):
    if a==b:
        return True


def quit(a):
    if a=="q":
        return True
            

game()
