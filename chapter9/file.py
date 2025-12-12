#types of file
'''
1. text files (.txt)
2. binary files(.jpg)

'''

f = open("chapter9/file.txt")
data = f.read()
print(data)
f.close()


import os
print("Searching here:", os.getcwd())
print(os.listdir())

st="saba siddiqui is a smart girl thikey h "
f=open("chapter9/myfile.txt", "w")
f.write(st)
f.close

#same can be written using with statement  like this :

with open("chapter9/file.txt") as f :
    print(f.read())