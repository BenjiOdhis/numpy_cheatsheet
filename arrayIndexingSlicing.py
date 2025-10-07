import numpy as np
arr = np.arange(10)
print(arr[2:7])
print(arr[:5])
print(arr[-3:])

matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])

print(matrix[0, 1])   # Access single element
print(matrix[1, :])   # Row 1
print(matrix[:, 2])   # Column 2
print(matrix[1:, 1:]) # Submatrix