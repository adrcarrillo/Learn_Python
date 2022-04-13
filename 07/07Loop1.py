# The while Loop in Action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 # The += operator is shorthand for current_number = curren_number + 1

# Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = "" # Empty string
while message != 'quit':
    message = input(prompt)
    print(message)
