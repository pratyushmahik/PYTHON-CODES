# Program to demonstrate matrix addition using nested lists and NumPy

# 1. Matrix Addition using Nested Lists

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Initialize the result list (2x2)
result_list = [[0, 0], [0, 0]]

# Perform addition
for i in range(len(A)):
    # Iterate through columns
    for j in range(len(A[0])):
        result_list[i][j] = A[i][j] + B[i][j]

print("---Matrix Addition using Nested Lists---")
print("Matrix A:", A)
print("Matrix B:", B)
print("Sum of matrices (using list):", result_list)

# 2. Matrix Addition using NumPy

import numpy as np

A_np = np.array([[1, 2], [3, 4]])
B_np = np.array([[5, 6], [7, 8]])

# Perform addition using NumPy's overloaded '+' operator
result_np = A_np + B_np

print("\n---Matrix Addition using NumPy---")
print("Matrix A (NumPy): \n", A_np)
print("Matrix B (NumPy): \n", B_np)
print("Sum of matrices (using NumPy): \n", result_np)