#string functions 

c= "hello superman"
#length of string
print(len(c))

#to uppercase
print(c.upper())

#to lower caseb
print(c.lower())

#remove extra spaces  
print(c.strip())

#replace string with new 
print(c.replace("superman", "sabah"))

#Returns the index of the first occurrence, or -1 if not found.
print(c.find("e"))

#Checks if a string begins or ends with something.
print(c.startswith('hel')) #true
print(c.endswith('man'))   #true 