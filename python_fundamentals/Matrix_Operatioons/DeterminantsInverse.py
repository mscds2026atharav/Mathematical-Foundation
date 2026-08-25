import numpy as np

n = int(input("Enter size of square matrix: "))

matrix = []

print("Enter matrix elements:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(float(input()))
    matrix.append(row)

A = np.array(matrix)

print("\nMatrix:")
print(A)

# Determinant
det = np.linalg.det(A)
print("\nDeterminant:", det)

# Inverse (if exists)
if det != 0:
    inverse = np.linalg.inv(A)
    print("\nInverse Matrix:")
    print(inverse)
else:
    print("\nInverse does not exist (Singular Matrix)")

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)