1.
class programmers:
    campany = "Microsoft"

    def __init__(self, name , prn , salary):
        self.name=name 
        self.prn =prn
        self.salary=salary 

employee=programmers("saba",45678,900000) 

print(employee.name , employee.prn, employee.salary)

2.
class calculator:
    def __init__(self,n):
        self.n =n

    def square(self):
        print(f"the square of {self.n*self.n}")


    def cube(self):
        print(f"the cube of {self.n*self.n*self.n}")    


    def squareroot(self):
        print(f"the squareroot of {self.n**1/2}")

a=calculator(5)        
a.square()
a.cube()
a.squareroot()
        


3.
class demo :
    a = 4
o=demo()
print(o.a) #prints the class attribute because instance attribute is not present 
o.a=1       #instance attribute is present
print(o.a) #prints the instance attribute  attribute because instance attribute is present 
print(demo.a) # class attribute does not change 

4.


