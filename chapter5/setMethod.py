set={ 3,6,"saba","df",90}

#Adds a single element.
set.add(34)


#Adds multiple elements at once.
set.update([23,"ramsha"])

#Deletes an element. Gives error if not present.
set.remove("df")

#Deletes an element but no error if missing.
set.discard(8)

#Removes a random element.
set.pop()

#Empties the set.
set.clear()

#Creates a shallow copy.
new_set = set.copy()

print(set)