name = "adrian Carrillo"
#Change the case
print(name.title())
#Upper case
print(name.upper())
#Lowe case
print(name.lower())

first_name = "adrian"
last_name = "carrillo"
#Concatenation
full_name = first_name + " " + last_name
print(full_name)
message = "Hello, I'm " + full_name.title() + "!"
print(message)

#Whitespaces
print("\t"+message)
print("Languages: \n\tPython\n\tJava\n\tJavaScript")


#In the real world, these stripping functions are used most often to clean up user input before it’s stored in a program.
#Stripping Whitespace
favorite_language1 = 'pyhton  '
print("String lenght: ", len(favorite_language1))
print("String lenght: ", len(favorite_language1.rstrip())) #right strip

favorite_language2 = ' python'
print(favorite_language2)
print(favorite_language2.lstrip()) #left strip

print(favorite_language1.strip()) #both sides strip
print(favorite_language2.strip()) #both sides strip
