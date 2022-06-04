filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string =  ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

pi_string =  ''
for line in lines:
    pi_string += line.strip() # Get rid the whitespaces by using strip()

print(pi_string)
print(len(pi_string))

print(pi_string[:20]) # Print only 20 digits