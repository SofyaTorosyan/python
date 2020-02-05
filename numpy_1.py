import numpy as np
l = [1, 2, 3]
# convert l to np array
nplist = np.array(l)
#print(nplist)

##### python list vs numpy array #####
L = [1, 2, 3]
NA = np.array(L)
print( 'List elements' )
for i in L:
    print(i)
print( 'numpy elements' )
for i in NA:
   print(i)
L1 = L + [4]
print('List1 after appending: ', L1)
# in case of numpy array + operator will add each element ov vector 4
NA1 = NA + [4]
print('NA1 after appending: ', NA1)

# NA.append(8) # ERROR
# numpy is used to do computations with N dimensional arrays

# addition
# sums each element
NA2 = NA + NA
print(NA2)

# list concatination
L2 = L + L
print(L2)

# multiplictaion
mult_NA = 2 * NA
print(mult_NA)

mult_list = 2 * L
print(mult_list)

# find power
power_NA = NA**2
print(power_NA)
# power_list = L**2 # error unsupported

sqrt_NA = np.sqrt(NA)
log_NA  = np.log(NA)
exp_NA  = np.exp(NA)

# loops are slower than numpy array operations
