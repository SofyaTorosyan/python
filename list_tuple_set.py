############### lists ###############
# lists are mutable
courses = ['History', 'Math', 'CompSci', 'Physics']
print("list: ",          courses)
print("list size: ",     len(courses))
print("first elements:", courses[0])

# negative indexing
print(courses[-1])

# print(courses[5]) out of range error
print(courses[0:2]) # second index is not included
print(courses[:2]) # the same as above

# adding item to the list
courses.append('Art')
courses.insert(0, 'English')
print("list after addition: ", courses)

# adding list to the list
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print("list after addition: ", courses)
print("first value is list: ", courses[0])

# adding multiple values to the list
courses.extend(courses_2)  # adds at the end 
print("list after extending: ", courses)

# removing item from the list 
courses.remove('Art')
print("list after removing: ", courses)
popped = courses.pop()
print("popped value: ", popped)


# sorting list
courses.reverse()
print("list in reverse order: ", courses)
courses.pop()
courses.sort() # sorting is done in alphabetical order # can't sort list of lists
print("list after sorting: ", courses)

numbers = [1, 2, 33, 1, 3]
numbers.sort()
print("numbers after sorting: ", numbers)
numbers.sort(reverse = True)
print("numbers after sorting in reverse order: ", numbers)

numbers_2 = [1, 4, 0, 2, 3]
sorted(numbers) # doesn't change numbers_2 : returns sorted bytearray
print("Sum: ", sum(numbers_2))
print("index of Math: ", courses.index('Math'))
# print("Value Error: ",   courses.index('Mathh'))
print("Does courses contain Math?: ", 'Math' in courses)

print("All items in courses: ")
for item in courses:
    print(item)

print("All items in courses <index, value>: ")
for index, item in enumerate(courses):
    print(index, item)
    
print("All items in courses <index, value>: ")
for index, item in enumerate(courses, start = 2): # start from second item
    print(index, item)
    
course_str  = ', '.join(courses)
course_str_ = ' - '.join(courses)
print("courses as string: ", course_str_)

courses_new = course_str_.split(' - ')
print("courses_new: ", courses_new)


############### tuples ############### 
# tuples can't be modified(immutable)

list_1 = [1, 2, 3]
list_2 = list_1
print("list_1: " , list_1)
print("list_2: " , list_2)

list_1[0] = 0 # list_2 is changed as they are THE SAME objects in memory
print("list_1: " , list_1)
print("list_2: " , list_2)

tuple_1 = (1, 2, 3)
tuple_2 = tuple_1
print("tuple_1: " , tuple_1)
print("tuple_2: " , tuple_2)
# tuple_1[0] = 0 # not supported. 

############### sets ############### 
# sets are values that are not ordered and there is no duplicate
courses_set = {1,28,3, 9}
print("set: ", courses_set)

courses_set_2 = {1,1,28,3, 6,8 }
print("set. No duplicate: ", courses_set_2)

# sets are optimized for membership check
print(1 in courses_set)
print("intersection: ", courses_set.intersection(courses_set_2))
print("union: ",        courses_set.union(courses_set_2))

# empty list
empty_list_1 = list()
empty_list_2 = []

# empty tuple 
empty_tuple_1 = tuple()
empty_tuple_2 = ()

# empty set
empty_set_1 = set()
empty_set = {} # NOT RIGHT it is empty dictionary 



    












