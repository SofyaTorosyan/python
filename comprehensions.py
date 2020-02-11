nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# write 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print ("my_list: ", my_list)

# above with comprehension
my_list = [n for n in nums ]
print ("(Comprehension) my_list: ", my_list)

# write n*n for each n in nums
list_2 = []
for n in nums:
    list_2.append(n*n)
print ("list_2: ", list_2)

# above with comprehension
list_3 = [n*n for n in nums ]
print ("(Comprehension) list_3: ", list_3)

# using a map + lambda
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable
list_4 = map(lambda n: n*n , nums)
print ("list_4: ", list_4)

# write n for each n in nums if n is even
list_5 = []
for n in nums:
    if n % 2 == 0:
        list_5.append(n)
print ("list_5: ", list_5)

# above with comprehensions
list_6 = [n for n in nums if n % 2 == 0]
print ("list_6: ", list_6)

# using filter + lambda
# instead of map ca use filter
list_7 = filter(lambda n: n % 2 == 0 , nums)
print ("list_4: ", list_7)

# write a (letter,num) pair for each letter in 'abcd' and each number '0123' example ('a', 0) ('a', 1) ('a', 2) ('a', 3)
list_8 = []
for letter in 'abcd':
    for num in range(4):
        list_8.append((letter,num)) # (letter, num) is tuple
print ("list_8: ", list_8)

list_9 = [(letter,num) for letter in 'abcd' for nufm in range(4)]
print("list_9: ", list_9)

# dictionary comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Betman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# The zip() function returns a zip object, which is an iterator of tuples
print zip(names, heros)

# get dict {'name': 'hero'} for each name, hero n zip (names, heros)
dict_1 = {}
for name, hero in zip(names, heros):
    dict_1[ name ] = hero
print("dict_1: ", dict_1)

#dict_2 = {name : hero for name, hero in zip(names, heros)}
#print("dict_2: ", dict_2)

# set comprehension
set_nums = [1,2,2,2, 3,4,5,6,7,7]
set_1 = set()
for n in set_nums:
    set_1.add(n)
print("set_1: ", set_1)

#set_2 = {n for n in set_nums}
#print("set_2: ", set_2)

# generator expressions
# yield n*n for each n in nums
def gen_func(nums):
    for n in nums:
        yield n*n
gen = gen_func(nums)

gen_2 = (n*n for n in nums)
for i in gen_2:
    print i
































