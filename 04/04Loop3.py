#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#Looping Through a Slice
print("\r")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three platers on my team:")
for player in players[:3]:
    print(player.title())

#Copying a List
print('\r')
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:] #copying, make a slice that starts at the first item and ends with the last item
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
print('\r')
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods #copying, This doesn't work.
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
