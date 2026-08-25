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

# Find inverse
det = np.linalg.det(A)

if det != 0:
    A_inv = np.linalg.inv(A)

    print("\nOriginal Matrix:")
    print(A)

    print("\nInverse Matrix:")
    print(A_inv)

    # Verify A × A^-1
    result = np.dot(A, A_inv)

    print("\nMatrix Multiplication (A × A^-1):")
    print(result)

    # Check if result is identity matrix
    if np.allclose(result, np.eye(n)):
        print("\nInverse Verified: Result is Identity Matrix")
    else:
        print("\nInverse Verification Failed")

else:
    print("Inverse does not exist")   