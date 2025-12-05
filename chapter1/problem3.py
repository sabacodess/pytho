#write a python program to print the content of direcrtory using the os module 


import os

path = "/"   # current directory

files = os.listdir(path)

for f in files:
    print(f)
