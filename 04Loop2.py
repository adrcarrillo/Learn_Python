#Using the range() Function
for value in range(1,5):
    print(value)

#Make a list
print("\r")
numbers = list(range(1,6))
print(numbers)
#List the even numbers; range(start, stop, step)
even_numbers = list(range(2,11,2))
print(even_numbers)

#Squares
print("\r")
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#Simple Statistics with a List of Numbers
print("\r")
digits = [1,2,3,4,5,6,7,8,9,0]
print(digits)

digits = list(range(1,10)) #Other way to build a list
digits.append(0)
print(digits)

digits = [1] #Other way to build a list
for x in range(1,9):
    x = x+1
    digits.append(x)
digits.append(0)
print(digits)

#Python Functions Min, Max and Sum
print("\r")
print(min(digits))
print(max(digits))
print(sum(digits))

#List Comprehensions
print("\r")
squares = [value**2 for value in range(1,11)]
print(squares)