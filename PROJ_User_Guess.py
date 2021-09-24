#COMPUTER GUESSES USER NUMBER

from random import randint

print ("I will guess your Number!")
g=randint(1,100)
c=1
print (g)

#USER INPUT
user=input("Is it high (H) or low (L) or Correct (C)?").lower()
while user!="c":
    if user=="h":
        c=c+1
        g=g-randint(1,10)
        print (g)
        user=input("Is it high H) or low (L) Lor Correct (C)?").lower()
    if user=="l":
        c=c+1
        g=g+randint(1,10)
        print(g)
        user=input("Is it high (H) or low (L) or Correct (C)").lower()

print (f"I guessed your number in {c} tries.")