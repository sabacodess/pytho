import random

computer = random.choice([1, -1, 0])
youstr= input("enter your choice :")
youdic ={"s": 1 , "w": -1 , "g":0}
reversedic={1:"snake ",-1:"water",0:"gun"}
you = youdic[youstr]

print(f" you choose {reversedic[you]} \n computer choose {reversedic[computer]}")

if(computer==you):
    print("its draw")
else:
    '''
    if(computer==-1 and you==1):-2
        print("you win")

    elif(computer==-1 and you==0):-1
        print("you lose")

    elif(computer==1 and you==-1):2
        print("you lose")

    elif(computer==1 and you==0):1
        print("you win")

    elif(computer==0 and you==-1):1
        print("you win")

    elif(computer==0 and you==1):-1
        print("you lose")
    
    '''
    if((computer- you) == -1 or (computer-you)==2):
        print("you lose")
    else:
        print("you win")    