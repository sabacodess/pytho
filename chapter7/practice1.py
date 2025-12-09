'''
  *
 ***
*****     
'''
# n=int(input("enter a number :"))

# for i in range(1,n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print("")

'''
*
**
***
'''
# n=int(input("enter a number :"))

# for i in range(1,n+1):
#     # print(" " * (n-i), end="")
#     print("*" * (1*i), end="")
#     print("")    

'''
***
* *
***
'''    

# n=int(input("enter a number :"))

# for i in range(1,n+1):
#     print("*" * (n) , end="")
#     print("*" + ""*(n-2) +"*")
#     print("*" * (n) , end="")
    

# n = int(input("enter a number : "))

# for i in range(1, n+1):
#     if i == 1 or i == n:               # first or last row
#         print("*" * n)
#     else:                              # middle rows
#         print("*" + " "*(n-2) + "*")


#problem8

n=int(input("enter  a num :"))

for i in range (10,1,-1):
    print(f"{n} x {i} = {n*(i)}")

