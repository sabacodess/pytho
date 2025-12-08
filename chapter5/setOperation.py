s1={1,6,5,4,}
s2={2,4,5,7,0}

#Combines elements of both sets. UNION
print(s1 | s2)
print(s1.union(s2))

#Common elements.INTERSECTION
print(s1 & s2)
print(s1.intersection(s2))

#Elements in A that are not in B. DIFFERENCE
print(s1-s2)

#Elements that are in A or B but not both.SYMMETRIC DIFFERENCE
print(s1 ^ s2)

#Checks if A is inside B.
s={1,2,3}
sq={1,2,3,4}
print(s.issubset(sq))

#Opposite of subset.
print(s.issuperset(sq))

#Checks if two sets share no common elements.
print(s.isdisjoint(s2))