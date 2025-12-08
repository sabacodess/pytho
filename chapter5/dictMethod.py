#methods 

d={
    "saba":99,
    "sharjeel":89,
    "wahid":78
}

#Returns all keys in the dictionary.
print(d.keys())

#Returns all values.
print(d.values())

#Returns key–value pairs as tuples.
print(d.items())

#Safe way to access a value. Doesn't give an error if key missing.
print(d.get("saba")) # its give none if this key doesn't exist 
print(d["saba"]) #returns an error

#Adds or updates key–value pairs.
print(d.update({"sharjeel":90}))
print(d)

#Removes a key and returns its value.
print(d.pop("wahid"))
print(d)

#Removes the last inserted key–value pair.
d.popitem()
print(d)

#Empties the dictionary.
d.clear()

#Creates a shallow copy of the dictionary.
new_d = d.copy()

#setdefault(key, default)
#If key exists → returns value
#If key doesn't exist → adds the key with default value

d.setdefault("course", "bca")
print(d)