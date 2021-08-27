favorite_languages = {
    'jean': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', #Acomma after the last key-value pair, ready to add a new key-value pair on the next line.
}
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

#Looping Through All Key-Value Pairs
print('\r')
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for k, v in user_0.items():
    print("\nKey: " + k)
    print("Value: " + v)

print('\r')
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")

#Looping Through All the Keys in a Dictionary
print('\r')
friends = ['phil', 'sarah']
for name in favorite_languages.keys(): #Using the keys() method, you can omit it if you wish
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!") #To access the current value of name as the key.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#Looping Through a Dictionary's Keys in Order
print('\r')
for name in sorted(favorite_languages.keys()): #sorted() function to get a copy of the keys in order.
    print(name.title() + ", thank you for taking the poll.")

#Looping Through All Values in a Dictionary
print('\r')
print("The following languages have mentioned:")
for language in favorite_languages.values():
    print(language.title())
print('\r')
for language in set(favorite_languages.values()): #set() function chooses without repetition
    print(language.title())