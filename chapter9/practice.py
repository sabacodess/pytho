1.

f = open("chapter9/poem.txt")
content = f.read()
if("twinkle" in content):
    print("twinkle is present in content ")
else :
    print("twinkle is not present in content ")    

2.

import random

def game():
    print("youre playing a game ..")  
    score = random.randint(1,67)
    with open("chapter9/highscore.txt")  as f :
        highscore = f.read()
        if(highscore !=""):
            highscore = int(highscore)
        else:
            highscore= 0
    print(f"your score:{score}")  
    if(score >highscore):
        with open("chapter9/highscore.txt", "w") as f:  
            f.write(str(score))     
    return score 
game() 
        
3.
def generatetables(n):
    table="" 
    for i in range (1,11):
        table+= f"{n} X {i} = {n*i}\n"

    with open(f"chapter9/tables/table_{n}.txt","w")  as f:
        f.write(table)  
for i in range (2,21):
    generatetables(i)


       

4. 
# word = "donkey"

words=["donkey","nonsense","chaos"]


with open("chapter9/word.txt", "r") as f:
   content= f.read()

for word in words:
    contentNew = content.replace(word,"####")
      
with open("chapter9/word.txt","w") as f :
       f.write(contentNew)


6.
with open("chapter9/word.txt") as f:
   lines= f.readlines()
linesno =1
for line in lines:
    if("python" in line):
        print(f"yes python is present ,lines no :{linesno}")
        break
    linesno += 1
else:
    print("python is not present")    




