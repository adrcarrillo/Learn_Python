#Tuples: Inmmutable list
#A tuple looks just like a list except you use parentheses instead of square brackets.
#Tuple object does not support item assignment
dimensions = (200,50)

print(dimensions[0])
print(dimensions[1])

#Looping Through All Values in a Tuple
print('\r')
for dimension in dimensions:
    print(dimension)

#Writing over a Tuple
print('\r')
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
