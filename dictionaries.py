######### dict #######
# dictionaries are <key~value> pairs
student = { 'name': 'Sofya', 'age': 23, 'courses': ['Python', 'Statistics']}
print(student)
print(student['name'])
# keys can be ANY IMMUTABLE type
# print(student['phone']) # key error 
print(student.get('phone')) # returns None for keys taht don't exist
print(student.get('phone', 'Not Found')) # with default value

# adding new entry
student['phone'] = '2222'
student.update({'name': 'Jane', 'age': 27})
print("Dict after updating: ", student)

del student['age']
print("Dict after deleteing age: ", student)

popped = student.pop('courses')
print("Popped value: ", popped)


# loop for all keys and values
print("Length: ", len(student)) # keys number
print("All items: ", student.items())
print("Keys: ",   student.keys())
print("Values: ", student.values())

for key, value in student.items():
    print(key, value)





