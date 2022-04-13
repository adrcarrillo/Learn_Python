class Dog(): # By convention, capitalized names refer to classes in Python.
    """A simple attempt to model a dog.""" # Doctring
    #  __init__() Special method Python runs automatically whenever we create
    # a new instance based on the class
    def __init__(self, name, age): 
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    # A function that’s part of a class is a method.
    # Every method call associated with a class automatically passes self, which 
    # is a reference to the instance itself
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# The __init__() method has no explicit return statement, but Python automatically
# returns an instance representing this dog.
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Calling the methods
my_dog.sit()
my_dog.roll_over()