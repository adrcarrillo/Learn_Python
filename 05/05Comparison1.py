cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper()) #Print bmw as BMW
    else:
        print(car.title())

#Ignoring Case When Checking for Equality
print('\r')
car = 'Audi'
print(car =='audi')
print(car.lower() == 'audi') #that the value stored in car has not been affected by the conditional test.

#Checking for Inequality
print('\r')
requested_topping = 'mushrooms'
if requested_topping != 'achovies':
    print('Hold the anchovies!')

#Numerical Comparisons
print('\r')
answer = 19
if answer != 42:
    print("That is not the correct answer. Please try again!")

print("That answer is less than 21: " + str(answer<21))
print("That answer is less than or equal to 21: " + str(answer<=21))
print("That answer is greater than 21: " + str(answer>21))
print("That answer is greater than or equal to 21: " + str(answer>=21))
print("That answer is equal to 21: " + str(answer==21))
print("That answer is equal to 19: " + str(answer==19))

#Check Multiple Conditions (AND)
print('\r')
age_0 = 22
age_1 = 18
print((age_0 >= 21) and (age_1 >= 21))
age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))

#Check Multiple Conditions (OR)
print('\r')
age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >= 21))
age_1 = 22
print((age_0 >= 21) or (age_1 >= 21))

#Checking Whether a Value Is in a List (IN)
print('\r')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#Checking Wheater a Value Is Not in a List (NOT IN)
print('\r')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
