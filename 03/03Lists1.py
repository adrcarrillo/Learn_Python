bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1]) #Return the last item in the list.
print(bicycles[-2]) #Return the second item from the end of the list.
print("\r")

#Concatenation
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
print("\r")

#Change elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print("\r")

#Appending Elements to the end of the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
print("\r")

#Build list with append()
motorcycles = []
motorcycles.append('honda')
motorcycles.append('suzuki')
print(motorcycles)
print("\r")

#Insert elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)
print("\r")

#Removing an Item using the del Statement
del motorcycles[3]
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print("\r")

#Removing an Item Using the pop() Method.
#When you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#Popping one item off the top of the stack
popped_motorcycle = motorcycles.pop()
last_owned = popped_motorcycle
print(motorcycles)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
#Popping the first one
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print("\r")

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
