#If-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#The if-elif-else Chain
print("\r")
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
elif age < 65:
    print("Your admission cost is $10.")
else:
    print("Your admission cost is $5.")

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".") #other way

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: #Does not requiere and else block at the end of an if-elif chain.
    price = 5
print("Your admission cost is $" + str(price) + ".")