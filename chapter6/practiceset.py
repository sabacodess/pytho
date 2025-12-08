#problem1
# a1 = input("enter a 1 number :")
# a2 = input("enter a 2 number :")
# a3 = input("enter a 3 number :")
# a4 = input("enter a 4 number :")

# if(a1>a2 and a1>a3 and a1>a4):
#     ( " greatest number a1 : ",a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#     (" greatest  number a2 :" , a2)   
# elif(a3>a1 and a3>a2 and a3>a4):
#     (" greatest  number a3 :" , a3) 
# elif(a4>a1 and a4>a2 and a4>a3):
#     (" greatest  number a4 :" , a4)     


#problem2

# marks1= int(input(" enter a marks :"))
# marks2= int(input(" enter a marks :"))
# marks3= int(input(" enter a marks :"))

# total_percentage=(100*( marks1* marks2*marks3))/300
# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     ("youre passed",total_percentage)
# else:
#     ("youre failed ",total_percentage)    


#problem3
# p1="make a alot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"

# message = input("Enter your comment :")

# if((p1 in message) or (p2 in message )or (p3 in message )or( p4 in message)):
#     ("this is comment spam")
# else:
#     (" this is not comment spam ")    


#problem4
# username= input("enter a username :")

# if(len(username)<10):
#     ("your username only contain  less than 10 charcaters")
# else:
#     (" yourusername contain more than 10 charcters")    


#problem5
# li  = [ "sharjeel","wahid","zayn","saba"]

# name=input("enter a name :")

# if( name in li):
#     ("your name is in list")
# else:
#     ("your name is not in a list ")    


#problem6

# marks=int(input("enter a marks: "))

# if(marks>= 90 and marks>= 100):
#     Grade="EX"
# elif(marks>=80 and marks>= 90):
#     Grade ="A "  
# elif(marks>=70 and marks>= 80):
#     Grade= "B"
# elif(marks>=60 and marks>= 70):
#     Grade = "C"
# elif(marks>=50 and marks>= 60):
#     Grade=" D " 
# elif(marks<50):
#     Grade="failed"      


# print("your grade is : ",Grade)    


#problem7

post=input("enter a post:")

if("Saba".lower() in post.lower()):
    print("this post is talking about saba")
else:
    print("this postiis not talking about saba ")    