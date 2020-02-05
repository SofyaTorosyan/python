import numpy as np
# 1-dim array
a = np.array([1, 2, 3])
# 2-dim array
b = np.array([[1, 2], [3, 4], [5, 6]])

print(a[0])
print(b[0]) # 1st element ` [1,2]
print(b[0][0])
print(b[0,0]) # the same as above
#create matrix
M = np.matrix([[1,2], [3,4], [5, 6]])
print( M )
# it is recommended to use numpy arrays istead of matrixes
# numpy array behaves the same as numpy matrix

# transpose of matrix
print("transpose of b")
print(b.T)

# dimensios
print("dimensions: ")
print(b.shape)

print(b.ndim) # dimesnion number
print("number of all elemets: ")
print(b.size)

print("type:")
print(b.dtype) # each element in b is int

d = np.array([1.1, 1.2])

print(d.dtype)

e = np.array([1, 2], dtype = np.float64)
print(e)
print(b.dtype)
print("Byte number for each element: ")
print(b.itemsize)

# find min of elements
print("Min value: ")
print(a.min())

print("Sum: ")
print(b.sum())

print(b.sum(axis = 0))  # sum in vertical 1+3+5 2+4+6
print(b.sum(axis = 1))  # sum in horizontal 1+2 3+4 5+6 
