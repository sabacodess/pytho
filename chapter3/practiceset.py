name = input("Enter a your name  :")

print(f"Good Afternoon {name} ")


letter=''' dear <|name|>,
          youre selected
          <|date|>
          '''

print(letter.replace("<|name|>","sharjeel").replace("<|date|>","06-Dec-2025"))


cust= " saba is a pro   girl"

print(cust.find("  "))

print(cust.replace("  "," "))

# strings are immutable which means that they can't be change


letter = "Dear harry ,\n\t This cource is very nice. \nThanks! "
print(letter)