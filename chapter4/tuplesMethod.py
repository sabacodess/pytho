a=(23,56,78,4,23,45)

no = a.count(23)
print(no)

ind= a.index(4)
print(ind)



#operations of tuples 

#concatenation  

t1=(23,56,"saba", 67,45, 90)
t2=("sharjeel",67,45,89,23)
t3= t1+t2
print(t3)

#indexing
print(t1[3]) 

#slicing
print(t1[2:4])

#membership
print("saba" in t1)

#iteration 
t4=("a","b","c")
for i in t4:
    print(i)

#min and max 
marks =(98,67,58,99,46)
minimum=min(marks)    
maximum=max(marks)
print(minimum)
print(maximum)

#length of tuple
length =len((7,8,9))
print(length)

#repetition 
ts= ("helllo",)*5
print(ts)


#packing
#Packing means putting multiple values together into a single tuple. Python does this automatically when you assign several values to one variable.

student = "saba", 21, "bca"
print(student)

#unpacking
#Unpacking means taking the values from a tuple and assigning them to multiple variables in one step.
name,age,course = student 
print(name)
print(course)

#another example  unpacking 
point=(12.4,78)
x,y=point
print("x=",x)
print("y",y)

