class user :
    name = "sabasiddqui"
    email = "saba@gmail.com"    #class attribute 
    isloggedIn = True


saba = user()                  #object creation    
saba.language = "js"          #instance attribute 

print(saba.language ,saba.name)


#self 
class user1 :
    name = "sabasiddqui"
    email = "saba@gmail.com"    #class attribute 
    isloggedIn = True


    def lang(self):
        print(f" the  language is {self.email}")


    @staticmethod
    def greet ():
        print("hello everyone")   
    
saba1= user1()     

saba1.lang() 
#user1.lang(saba)   
    




