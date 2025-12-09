#function definition

def avg():
    a =int(input("enter a number "))
    b =int(input("enter a number "))
    c =int(input("enter a number "))

    average= (a+b+c)/3
    print(average)

    
avg() #function calling


# quick quiz

def goodDay(name):
    print("goodday" , name)
goodDay("sharjeel")    


#two types of functions 
'''
1. built in function (already in python )
2.user defined function ( defined by users )

'''

#default parameters
def goodDay(name , ending="thank you"):
    print("goodday" , name)
    print(ending)
goodDay("sharjeel") 
