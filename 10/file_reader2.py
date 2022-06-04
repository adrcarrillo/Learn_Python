filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() # Make a list

for line in lines:
    print(line.rstrip())