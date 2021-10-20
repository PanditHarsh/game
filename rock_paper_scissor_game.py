import random
def game(comp,you):
    if comp=='r':
        if you=='r':
            return None
        elif you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=='p':
            return None
        elif you=='s':
            return True
        elif you=='r':
            return False
    elif comp=='s':
        if you=='s':
            return None
        elif you=='r':
            return True
        elif you=='p':
            return False

print("Computer turn: rock , paper or scissor ?")
randguess = random.randint(1,3)

if randguess==1:
    comp='r'
elif randguess==2:
    comp='p'
elif randguess==3:
    comp='s'

you = input("Your turn: rock(r) paper(p) or scissor(s)\n")
print(f"Computer have choosen {comp} and you have choosen {you}")
a=game(comp,you)

if a==None:
    print("The game is a tie ")
elif a:
    print("You won!")
else:
    print("You loose!")
