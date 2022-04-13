#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
print("\r")

#Sorting in reverse alphabetical
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars)
print('\r')

#Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)
print('\r')

#Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
print('\r')

#Lenght of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("The lenght of the list is: " + str(len(cars)))
