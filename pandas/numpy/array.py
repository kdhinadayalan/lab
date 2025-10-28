import numpy as np

# Create NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Access and slicing
print("First element:", arr[0])
print("First 3 elements:", arr[:3])
print("Last 2 elements:", arr[-2:])

# Basic operations
print("Add 5 to each:", arr + 5)
print("Multiply by 2:", arr * 2)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())

A = np.array([[1, 2,],
              [5, 6,]])

B = np.array([[9, 10],
              [13,14]])

# Addition
print("A + B:\n", A + B)

# Subtraction
print("A - B:\n", A - B)

# Element-wise multiplication
print("A * B:\n", A * B)

# Matrix multiplication
print("A x B:\n", np.dot(A, B))

# Transpose
print("Transpose of A:\n", A.T)

