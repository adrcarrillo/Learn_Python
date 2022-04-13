# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit when you are finished.) "

while True: # Start conditional
    city = input(prompt)

    if city == 'quit':
        break # You can use break statement in any of Python's loops
    else:
        print("I'd love to go to " + city.title() + "!")