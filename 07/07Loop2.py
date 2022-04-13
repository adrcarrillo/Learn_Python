# Using a Flag
# For many different events could cause the program to stop running
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True # This variable called a Flag
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)