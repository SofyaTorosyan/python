# strings
my_message_1 = "Hello World"
my_message_2 = 'David\'s pen'
print(my_message_1)
print(len(my_message_1))
# print(my_message_1[11]) # out of range error
print(my_message_1[0:5])  # 0 is included, 5 is not included [0:5)
print(my_message_1[:5])   # same as above
print(my_message_1[6:11]) # 
print(my_message_1[6:])   # same as above

# some methods
print(my_message_1.lower())
print(my_message_1.upper())
print(my_message_1.count('l'))
print(my_message_1.find('W'))
print(my_message_1.replace('World', "World!!!!!"))
print(my_message_1)

# string concatination
greeting = 'Hello'
name     = 'Sofya'
new_message_1 = greeting + ', ' + name + '. Welcome!!!'
new_message_2 = '{}, {}. Welcome!!!'.format(greeting, name) # the same as abpve. {} are called placeholders
print(new_message_2)

print(dir(name)) # shows all methods used here on name
print(help(str)) # shows all methods of string
print(help(str.lower)) # shows lower method description

