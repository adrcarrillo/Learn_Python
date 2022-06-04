filename = 'programming.txt'

with open(filename, 'w') as file_object: # Argument 'w' is in wrire mode. 'r' read mode is the default
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")