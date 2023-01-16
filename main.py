import random 
print("Let's draw straws!")
names_string = input("Please enter everyone's name separated by a comma.\n")
names = names_string.split(", ")
people = int(len(names) - 1)
pick = int(random.randint(0, people))
print(names[pick] + " drew the short straw.")