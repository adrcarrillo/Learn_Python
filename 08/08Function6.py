# Modifying a List in a Function
# Start with some dseigns that need to be printed.
print('\r')
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# Modiying a List in a Function. Reorganize the code by writing two functions.
print('\r')
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Preventing a Function from Modifying a List
# Using function_name(list_name[:])
# It’s more efficient for a function 
# to work with an existing list to avoid using the time and memory needed to 
# make a separate copy, especially when you’re working with large lists.
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)