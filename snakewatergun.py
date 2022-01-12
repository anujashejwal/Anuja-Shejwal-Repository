import random

def gameWin(comp,you):
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

    elif comp=='w':
        if you=='s':
            return False
        elif you=='s':
            return True

    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

randomNo=random.randint(1,2)

comp=input('comp turn:snake(s),water(w),gun(g)?: ')
randNo=random.randint(1,3)
print(randNo)

if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input('player turn:snake(s),water(w),gun(g)?: ')
a= gameWin(comp,you)

if a==None:
    print('the game is tie')
elif a:
    print('you win')
else:
    print('you lose')