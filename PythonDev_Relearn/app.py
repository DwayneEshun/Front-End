name  = 'Jennifer'
print(name[1:-1])
# BUILT IIN METHODS FOR STRINGS
'''name.upper()
name.lower()
name.find('J')
name.replace()
"red" in name
name.title()
'''

#MATH FUNCTIONS
'''import math
import math makes it possible to use .math functions, eg
math.sqrt()
math.floor()
math.factorial() #etc!!
round() # Rounds to the nearest integer
abs() #always returns the positive int
'''
#If statements!
#Program 1
'''temp = input("whats the temperature?\n");

if int(temp) >= 30:
    print("It's a hot day!/n Drink Plenty of water");
elif int(temp) <= 16:
    print("It's a cold day'/n wear warm clothes")
else:
    print("It's a lovely day!!")
'''

#Program 2
'''name = input("Enter your name: ")
namelen = len(name)
if namelen < 3:
    print("Name must be more than 3 Characters")
elif namelen > 50:
    print("This is too much")
else:
    print(f"Hello! {name}")
'''
#program 3- The double edged weight calculator
'''weight = float(input("Enter your weight: "))
userChoice = input("(K)g or (L)bs: ")
if userChoice == "k" or userChoice == "K": #You can also use userChoice.upper() or userChoice.lower
    print(f"You are {weight * 2.205}Lbs")
elif userChoice.upper() == "L":
    print(f"You weigh {weight * 0.454}Kg")

t = "THANK YOU"
print(t.upper())
'''

#While Loops
#program 4- The guessing game
'''secret_number = 7
entered = 0
limit = 3
while entered < limit:
    guess = int(input("Enter your guess: "))
    entered += 1
    if guess == secret_number:
        print("You guessed right!!")
        break
    else:
        print("You guessed wrong")
else:
    print("Sorry! You Ran out of attempts")
'''




print("Type 'help' to show car options")
user_input = ""
while True:
    user_input = input(">")
    if user_input == "start":
        print("Engine Started") 
    elif user_input == "stop":
        print("Engine stopped")
    elif user_input == "help":
        print("""
Start - To start Engine
Stop - To stop Engine
Quit - To exit car                          
""")
    elif user_input == "quit":
     break
    else:
       print("Sorry I don't understand ")
