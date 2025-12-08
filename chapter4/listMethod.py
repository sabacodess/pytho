friends=["saba ","sharjeel","zoya", 1234,12.4 , True , 3]


#Adds an item at the end.
friends.append("adeeb")


#Adds an item at a specific position.
friends.insert(4,"assssl")

#Reverses the list.
friends.reverse()

#Counts how many times an item appears.
print(friends.count("saba "))

#Removes and returns an item If no index, removes last element.
friends.pop(1)

#deletes the first matching element from the list.
friends.remove("zoya")

print(friends) 

li=[2,8,9,4,0,56,89]

# li.extend(friends)

#Sorts the list in ascending order.
li.sort()

#Returns the first index of the given item.
print(li.index(56))

#Makes a shallow copy of the list.
lists=li.copy()
print(lists)

#takes another list (or any iterable) and adds all its elements to the end of your list.
li.extend(friends)

#Empties the list.
#li.clear()
print(li)