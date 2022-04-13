#Dictionaries
alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

#Accesing values in a Dictionary
print('\r')
new_points = alien_0['points']
print("You just earn " + str(new_points) +" points!")
#Adding New Key-Value Pairs
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Staring with an Empty Dictionary
print('\r')
alien_0 ={}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#Modifiying Values
alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0 = {'color':'yellow'} #Change to yellow
print("The alien is " + alien_0['color'] + ".")

#Adding speed
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
#Move the alien to the right
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3
#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#Removing Key-Value Pairs
print('\r')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
