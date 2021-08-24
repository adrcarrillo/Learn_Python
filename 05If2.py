#Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")

#Using if Statements with Lists
print("\r")
requested_toppings = ['mushrooms', 'green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("Finished making your pizza!")

#Checking That a List Is Not Empty
print("\r")
requested_toppings = [] #Empty List
if requested_toppings: #Check whether a list is empty before running a for loop
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("\r")
requested_toppings = ['mushrooms', 'extra cheese'] #Not Empty List
if requested_toppings: #Check whether a list is empty before running a for loop
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Multiple Lists
print("\r")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("Finished making your pizza!")