
#if else statement 

age= int(input("enter your age :"))

# if(age>=18):
#     print("yep! you can drive ")
# else:
#     print("ohno!  you can't drive") 

# if - elif - else ladder 
 
if(age>=18):
    print("yep! you can drive ")
elif(age==0):
    print("enter a valid  age ,\" 0\" is not a valid age  ")    
elif(age<0):
    print("enter a valid age , age can't be neagtive ")    
else:
    print("you can't drive")
