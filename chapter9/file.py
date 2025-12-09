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