language = 'Java'
if language == 'Python':
   print("Language is python")
elif language == 'Java':
    print("Language is Java")
elif language == 'C++':
    print("Language is C++")
else:
    print("Langauage is not python")
   
# doesnot have switch elif is enough

# boolean  operations
user = 'Admin'
logged_in = True

# and
if user == 'Admin' and logged_in:
    print("Admin page")
else:
    print("Bad...")
    
# or
if user == 'Admin' or logged_in:
    print("Admin page")
else:
    print("Bad...")
    
if not logged_in: # if !logged_in == true 
    print("not logged")
    
# object identity -- whether they are the same in memory
first  = [0, 1, 0]
second = [0, 1, 0]

print("Checking identity")
print(first == second)
print(first is second) # false as they are NOT the same in memory
print("Ids of first and second are different: ")
print(id(first))
print(id(second))

second = first
print("Ids of first and second are the same: ")
print(id(first))
print(id(second))



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    