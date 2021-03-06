# Using input() to Accept Numerical Input
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# The Modulo Operator
# The modulo operator tells you what the remainder.
print('\r')
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number) # convert from string to integer

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
