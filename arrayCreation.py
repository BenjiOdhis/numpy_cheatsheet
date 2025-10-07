import numpy as np
#creating an array from lists.tuples
positons =np.array((1,2,3))
print(positons)
#array of zeros(l,w,h)
grid0=np.zeros((2,3))
print(grid0)
#of ones
grid1=np.ones((2,5,3))
print(grid1)
#filled with constant((l,w,h),constant)
completion=np.full((3,2),7)
print(completion)
#range with steps((l,w,steps)
array1d=np.arange(0,20,2)
print(array1d)
#evenly spaced values
space = np.linspace(0,10,5)
print(space)
#identity matrix
identity= np.eye(3)
print(identity)
#random floats
floats=np.random.rand(2,3)
#random integers
integers=np.random.randint(0,100,(2,3))
print(floats)
print(integers)