my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print my_list[0]

# extract ranges from list
print my_list[0:5]
print my_list[-7:-2]
print my_list[1:] # to the end
print my_list[2:-1:2] # 3rd element is step
print my_list[-1:2:-1] # in reverse order from 9 to 3
# entire list
print my_list[::-1]

sample_url = 'https://some_company.com'
print sample_url

# reverse the url
print sample_url[::-1]

#get toplevel domain .com
print sample_url[-4:]

# print without http://
print sample_url[7:]

#print url without http:// or top level domain
print sample_url[7:-4]


####### SORTING #######
# sorting lists
li = [9, 1, 2, 3, 6, 7, 8, 5, 4]
s_li = sorted(li)
print('Sorted list: ', s_li)
print('Original list: ', li)
li.sort()
s_li = li.sort() # no return s_li is None
print('Original list: ', li)


# sorting in reverse order
s_li = sorted(li, reverse = True)
print('Sorted list: ', s_li)
print('Original list: ', li)
li.sort(reverse = True)
print('Original list: ', li)

# sort method gives flexibility
tup = (9, 1, 2, 3, 6, 7, 8, 5, 4)
# tuples have no sort functions
s_tup = sorted(tup)
print('Sorted tuple: ', s_tup)

di = {'name': 'John', 'job': 'programming', 'age': '12' }
s_di = sorted(di)
print ('Sorted dict: ', s_di)



list = [-6, -5, -1, 1, 2, 3]
s_list = sorted(list, key = abs) # runs everything in abs value
print(s_list)






























































