#problem1

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b 
    elif(c>a and c>b):
        return c
a=4
b=5
c=7

print(greatest(a,b ,c))

#problem 2
#c= 5*(f-32)/9

def f_to_c(f):
    return  5*(f-32)/9
f=int(input("enter a temp in F :"))
c= f_to_c(f)
print(f"{c,2}")


#problem3
'''
sum(1)=1
sum(2)= 2+1
sum(3)= 3+2+1
sum(4)=4+3+2+1
sum(5)=5+4+3+2+1

sum(n)=n+ sum(n-1)
'''

def sum(n):
    if(n==1 or n==0):
        return 1 
    return n+ sum(n-1)
print(sum(4))


#problrm4
'''
***
**
*
'''
   

def stars(n):
    if(n==0):
        return
    print("*"*n)
    stars(n-1)
stars(5)    

#problem5

def inch_to_cms(inch):
    return inch* 2.54

inch = int(input("enter a number in inches"))
print(inch_to_cms(inch))

#problem6
def rem(l , word):
    n=[]
    for item in l :
        if not (item == word):
            n.append(item.strip(word))
    return n        
l=["harry" ,"rohan", "an","anshika","saba"]
print(rem(l,"an"))