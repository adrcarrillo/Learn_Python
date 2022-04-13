# input() Function works
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Writing clear prompts
name = input("Please enter your name: ")
print("Hello, " + name + "!")
print('\r')
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name "
name = input(prompt)
print("Hello, " + name + "!")

# Using int() to Accept Numerical Input
print('\r')
age = input("How old are you? ") # Input by user is string
age = int(age)
print("Age >= 18?: " + str((age >= 18)))
