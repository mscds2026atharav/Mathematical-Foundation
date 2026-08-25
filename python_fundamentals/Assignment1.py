# Numerical Computation and Precision 

# %%
# 1. Accept a positive number and compute its square root. 
import math
x=int(input("Enter a +ve number: "))
y=math.sqrt(x)
print(y)

# %%
# 2. Display the result rounded to 2, 5, 10, and 15 decimal places. 
num = float(input("Enter a number: "))

print(f"Rounded to 2 decimal places : {num:.2f}")
print(f"Rounded to 5 decimal places : {num:.5f}")
print(f"Rounded to 10 decimal places: {num:.10f}")
print(f"Rounded to 15 decimal places: {num:.15f}")

# %%
# 3. Investigate floating-point arithmetic by evaluating expressions involving decimal numbers and explain your observations. 
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.3 - 0.2 =", 0.3 - 0.2)
print("0.1 * 3 =", 0.1 * 3)

print("Comparison")
print("0.1 + 0.2 == 0.3 :", (0.1 + 0.2) == 0.3)

# %%
# 4. Determine the machine epsilon for floating-point numbers using Python. 
epsilon = 1.0

while 1.0 + epsilon != 1.0:
    epsilon /= 2

epsilon *= 2

print("Machine Epsilon for float =", epsilon)

# Vector Operations 

# %%
# 1. Accept two vectors of equal length from the user. 
n = int(input("Enter the number of elements: "))

vector1 = []
vector2 = []

print("Enter elements of Vector 1:")
for i in range(n):
    vector1.append(float(input()))

print("Enter elements of Vector 2:")
for i in range(n):
    vector2.append(float(input()))

print("Vector 1:", vector1)
print("Vector 2:", vector2)

# %%
# 2. Perform vector addition and subtraction. 
n = int(input("Enter the number of elements: "))

v1 = []
v2 = []

print("Enter elements of Vector 1:")
for i in range(n):
    v1.append(int(input()))

print("Enter elements of Vector 2:")
for i in range(n):
    v2.append(int(input()))

addition = []
subtraction = []

for i in range(n):
    addition.append(v1[i] + v2[i])
    subtraction.append(v1[i] - v2[i])

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Vector Addition:", addition)
print("Vector Subtraction:", subtraction)

# %%
# 3. Compute element-wise multiplication. 
n = int(input("Enter the number of elements: "))

v1 = []
v2 = []

print("Enter elements of Vector 1:")
for i in range(n):
    v1.append(int(input()))

print("Enter elements of Vector 2:")
for i in range(n):
    v2.append(int(input()))

result = []

for i in range(n):
    result.append(v1[i] * v2[i])

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Element-wise Multiplication:", result)

# %%
# 4. Compute the dot product. 
n = int(input("Enter the number of elements: "))

v1 = []
v2 = []

print("Enter elements of Vector 1:")
for i in range(n):
    v1.append(int(input()))

print("Enter elements of Vector 2:")
for i in range(n):
    v2.append(int(input()))

dot_product = 0

for i in range(n):
    dot_product += v1[i] * v2[i]

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Dot Product:", dot_product)

# %%
# 5. Calculate the Euclidean norm of each vector. 
import math

n = int(input("Enter the number of elements: "))

v1 = []
v2 = []

print("Enter elements of Vector 1:")
for i in range(n):
    v1.append(int(input()))

print("Enter elements of Vector 2:")
for i in range(n):
    v2.append(int(input()))

# Calculate Euclidean norm
norm1 = math.sqrt(sum(x*x for x in v1))
norm2 = math.sqrt(sum(x*x for x in v2))

print("Vector 1:", v1)
print("Euclidean Norm of Vector 1:", norm1)
print("Vector 2:", v2)
print("Euclidean Norm of Vector 2:", norm2)

# %%
# 6. Compute the cosine similarity between the vectors.

import math

n = int(input("Enter the number of elements: "))

v1 = []
v2 = []

print("Enter elements of Vector 1:")
for i in range(n):
    v1.append(int(input()))

print("Enter elements of Vector 2:")
for i in range(n):
    v2.append(int(input()))

# Dot product
dot_product = sum(v1[i] * v2[i] for i in range(n))

print("Dot product: ", dot_product)

# Euclidean norms
norm1 = math.sqrt(sum(x*x for x in v1))
norm2 = math.sqrt(sum(x*x for x in v2))

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Euclidean norm of vector 1: ",norm1)
print("Euclidean norm of vector 2: ",norm2)

# Cosine similarity
cosine_similarity = dot_product / (norm1 * norm2)

print("Cosine Similarity:", cosine_similarity)

# Matrix Operations 

# %%
# 1. Accept the dimensions and elements of a matrix. 
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)
    
# %%
# 2. Compute its transpose. 
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

transpose = []

for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

print("Original Matrix:")
for row in matrix:
    print(row)

print("Transpose Matrix:")
for row in transpose:
    print(row)
    
# %%
# %%
# 3. If the matrix is square:
#    - Compute its determinant
#    - Find its inverse (if it exists)
#    - Compute its eigenvalues and eigenvectors

import numpy as np

n = int(input("Enter size of square matrix: "))

matrix = []

print("\nEnter matrix elements:")

for i in range(n):
    row = []
    for j in range(n):
        value = float(input(f"Element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

A = np.array(matrix)

print("\nMatrix:")
print(A)

# Determinant
det = np.linalg.det(A)
print(f"\nDeterminant: {det:.3f}")

# Inverse (if exists)
if np.isclose(det, 0):
    print("\nInverse does not exist (Singular Matrix)")
else:
    inverse = np.linalg.inv(A)
    print("\nInverse Matrix:")
    print(inverse)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# %%
# %%
# 4. Verify the inverse by matrix multiplication.

import numpy as np

# Display numbers with 3 decimal places
np.set_printoptions(precision=3, suppress=True)

n = int(input("Enter size of square matrix: "))

matrix = []

print("\nEnter matrix elements:")

for i in range(n):
    row = []
    for j in range(n):
        value = float(input(f"Element [{i+1}][{j+1}]: "))
        row.append(value)
    matrix.append(row)

A = np.array(matrix)

# Find determinant
det = np.linalg.det(A)

if np.isclose(det, 0):
    print("\nInverse does not exist (Singular Matrix)")
else:
    # Find inverse
    A_inv = np.linalg.inv(A)

    print("\nOriginal Matrix:")
    print(A)

    print("\nInverse Matrix:")
    print(A_inv)

    # Verify A × A⁻¹
    result = np.dot(A, A_inv)

    print("\nMatrix Multiplication (A × A⁻¹):")
    print(result)

    # Check if the result is an identity matrix
    if np.allclose(result, np.eye(n)):
        print("\nInverse Verified: Result is Identity Matrix")
    else:
        print("\nInverse Verification Failed")


# Probability Through Simulation

# %%7
# 1. Accept the number of trials from the user.
trials_num = int(input("Enter number of trials: "))
print("Number of trials:", trials_num)

# %%
# 2. Simulate the experiment of rolling two dice repeatedly.
import random

trials_num = int(input("Enter number of trials: "))

for i in range(trials_num):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print(f"Roll {i+1}: Die 1 = {die1}, Die 2 = {die2}, Sum = {total}")

# %%
# 3. Estimate the probability of obtaining a user-specified sum.
import random

target_sum = int(input("Enter the desired sum (2-12): "))
trials_num = int(input("Enter number of simulations: "))

if target_sum < 2 or target_sum > 12:
    print("Invalid sum! Please enter a value between 2 and 12.")
else:
    count = 0

    for _ in range(trials_num):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        if die1 + die2 == target_sum:
            count += 1

    probability = count / trials_num

    print(f"\nTarget Sum: {target_sum}")
    print(f"Number of Simulations: {trials_num}")
    print(f"Occurrences: {count}")
    print(f"Estimated Probability: {probability:.4f}")

# %%
# 4. Compare the simulated probability with the theoretical probability.

# Number of ways to obtain each sum with two dice
theoretical = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# The simulated probability should already be calculated in the previous cell
# using the variables: target_sum and probability

theoretical_probability = theoretical[target_sum]

print("\nComparison of Probabilities")
print(f"Target Sum           : {target_sum}")
print(f"Simulated Probability: {probability:.6f}")
print(f"Theoretical Probability: {theoretical_probability:.6f}")
print(f"Difference           : {abs(probability - theoretical_probability):.6f}")

if abs(probability - theoretical_probability) < 0.01:
    print("Result: The simulated probability is close to the theoretical probability.")
else:
    print("Result: Increase the number of trials for a more accurate estimate.")

# %%
# 5. Plot the frequency distribution of all possible sums.

import random
import matplotlib.pyplot as plt

# Number of simulations
trials_num = int(input("Enter number of simulations: "))

# Dictionary to store frequencies of sums (2 to 12)
frequency = {i: 0 for i in range(2, 13)}

# Simulate rolling two dice
for _ in range(trials_num):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    frequency[total] += 1

# Display frequencies
print("\nFrequency Distribution:")
for s in range(2, 13):
    print(f"Sum {s}: {frequency[s]}")

# Plot the frequency distribution
plt.figure(figsize=(8, 5))
plt.bar(frequency.keys(), frequency.values(), edgecolor="black")
plt.title("Frequency Distribution of Sums of Two Dice")
plt.xlabel("Sum")
plt.ylabel("Frequency")
plt.xticks(range(2, 13))
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Function Analysis and Visualization

# %%
# 1. Accept the coefficients of a polynomial function from the user.

degree = int(input("Enter the degree of the polynomial: "))

coefficients = []

print(f"Enter the {degree + 1} coefficients (from highest degree to constant term):")

for i in range(degree + 1):
    coef = float(input(f"Coefficient of x^{degree - i}: "))
    coefficients.append(coef)

print("\nPolynomial Coefficients:")
print(coefficients)

# %%
# 2. Plot the function over a suitable range.

import numpy as np
import matplotlib.pyplot as plt

# Create polynomial
p = np.poly1d(coefficients)

# Generate x values
x = np.linspace(-10, 10, 400)

# Compute y values
y = p(x)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Polynomial", linewidth=2)
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Polynomial Function")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.grid(True)
plt.legend()
plt.show()

# %%
# 3. Estimate the derivative numerically.

import numpy as np

# Create polynomial from coefficients
p = np.poly1d(coefficients)

# Input point where derivative is required
x0 = float(input("Enter the value of x: "))

# Small step size
h = 1e-5

# Central difference formula
derivative = (p(x0 + h) - p(x0 - h)) / (2 * h)

print(f"\nEstimated derivative at x = {x0} is {derivative:.6f}")

# %%
# 4. Plot the polynomial and its derivative on the same graph.
import numpy as np
import matplotlib.pyplot as plt

# Create polynomial from coefficients
p = np.poly1d(coefficients)

# Compute derivative polynomial
dp = np.polyder(p)

# Generate x values
x = np.linspace(-10, 10, 400)

# Evaluate functions
y = p(x)
dy = dp(x)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Polynomial", linewidth=2)
plt.plot(x, dy, label="Derivative", linewidth=2)

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.title("Polynomial and Its Derivative")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show()

# %%
# 5. Identify approximate stationary points.

import numpy as np
import matplotlib.pyplot as plt

# Create polynomial and its derivative
p = np.poly1d(coefficients)
dp = np.polyder(p)

# Generate x values
x = np.linspace(-10, 10, 1000)

# Evaluate polynomial and derivative
y = p(x)
dy = dp(x)

# Find points where derivative is approximately zero
tolerance = 0.05
indices = np.where(np.abs(dy) < tolerance)[0]

# Remove duplicate nearby points
stationary_x = []
for i in indices:
    if not stationary_x or abs(x[i] - stationary_x[-1]) > 0.1:
        stationary_x.append(x[i])

stationary_y = [p(val) for val in stationary_x]

# Print stationary points
print("Approximate Stationary Points:")
for sx, sy in zip(stationary_x, stationary_y):
    print(f"({sx:.3f}, {sy:.3f})")

# Plot
plt.figure(figsize=(8,5))
plt.plot(x, y, label="Polynomial")
plt.plot(x, dy, label="Derivative")

# Mark stationary points
plt.scatter(stationary_x, stationary_y, color="red", label="Stationary Points", zorder=5)

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Polynomial and Approximate Stationary Points")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

# Statistical Analysis of Data

# %%
# 1. Accept a list of numerical values from the user.

n = int(input("Enter the number of values: "))

data = []

print("Enter the values:")
for i in range(n):
    data.append(float(input()))

print("\nData:", data)

# %%
# 2. Compute Mean, Median, Mode, Variance, and Standard Deviation.

import statistics

mean = statistics.mean(data)
median = statistics.median(data)

try:
    mode = statistics.mode(data)
except statistics.StatisticsError:
    mode = "No unique mode"

variance = statistics.variance(data)      # Sample variance
std_dev = statistics.stdev(data)          # Sample standard deviation

print("\nStatistical Measures")
print(f"Mean               : {mean:.2f}")
print(f"Median             : {median:.2f}")
print(f"Mode               : {mode}")
print(f"Variance           : {variance:.2f}")
print(f"Standard Deviation : {std_dev:.2f}")

# Descriptive Statistics Without Libraries

# %%
# 1. Accept a dataset from the user.

n = int(input("Enter the number of values: "))

data = []

print("Enter the values:")
for i in range(n):
    data.append(float(input()))

print("\nDataset:", data)

# %%
# 2. Write your own functions to compute statistics.

import math

# Mean
def mean(data):
    return sum(data) / len(data)

# Median
def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

# Mode
def mode(data):
    freq = {}

    for value in data:
        freq[value] = freq.get(value, 0) + 1

    max_freq = max(freq.values())

    modes = [key for key, value in freq.items() if value == max_freq]

    if max_freq == 1:
        return "No Mode"

    return modes

# Range
def data_range(data):
    return max(data) - min(data)

# Standard Deviation (Sample)
def standard_deviation(data):
    m = mean(data)

    variance = sum((x - m) ** 2 for x in data) / (len(data) - 1)

    return math.sqrt(variance)

print("\nStatistics (Without Libraries)")
print(f"Mean               : {mean(data):.2f}")
print(f"Median             : {median(data):.2f}")
print(f"Mode               : {mode(data)}")
print(f"Range              : {data_range(data):.2f}")
print(f"Standard Deviation : {standard_deviation(data):.2f}")

# %%
# 3. Compare the results with NumPy and Statistics library.

import numpy as np
import statistics

print("\nComparison with Libraries")

print(f"Mean")
print(f"Custom      : {mean(data):.2f}")
print(f"NumPy       : {np.mean(data):.2f}")

print("\nMedian")
print(f"Custom      : {median(data):.2f}")
print(f"NumPy       : {np.median(data):.2f}")

try:
    lib_mode = statistics.mode(data)
except statistics.StatisticsError:
    lib_mode = "No Unique Mode"

print("\nMode")
print(f"Custom      : {mode(data)}")
print(f"Statistics  : {lib_mode}")

print("\nRange")
print(f"Custom      : {data_range(data):.2f}")
print(f"NumPy       : {np.ptp(data):.2f}")

print("\nStandard Deviation")
print(f"Custom      : {standard_deviation(data):.2f}")
print(f"NumPy       : {np.std(data, ddof=1):.2f}")


# Linear Algebra Concepts

# %%
# 1. Accept a matrix from the user.

import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

print("Enter the matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(float(input(f"Element [{i+1}][{j+1}]: ")))
    matrix.append(row)

A = np.array(matrix)

print("\nMatrix:")
print(A)

# %%
# 2. Determine the rank of the matrix.

rank = np.linalg.matrix_rank(A)

print("Rank of the matrix:", rank)

# %%
# 3. Check whether the columns are linearly independent.

rank = np.linalg.matrix_rank(A)

if rank == A.shape[1]:
    print("The columns are linearly independent.")
else:
    print("The columns are linearly dependent.")

# %%
# 4. Explain the implications of linear dependence.

print("\nImplications of Linear Dependence in Machine Learning:\n")

if rank == A.shape[1]:
    print("- All features provide unique information.")
    print("- Models are generally more stable.")
    print("- Coefficients are easier to interpret.")
else:
    print("- Some features are redundant.")
    print("- Multicollinearity may occur.")
    print("- Regression coefficients can become unstable.")
    print("- The matrix may become singular, making inversion difficult.")
    print("- Removing redundant features or applying PCA can improve performance.")

# %%
# 5. Compute the condition number and discuss the result.

if A.shape[0] == A.shape[1]:

    cond = np.linalg.cond(A)

    print(f"\nCondition Number: {cond:.4f}")

    if cond < 10:
        print("The matrix is well-conditioned.")
    elif cond < 1000:
        print("The matrix is moderately conditioned.")
    else:
        print("The matrix is ill-conditioned.")
        print("Small changes in the data may produce large changes in the solution.")

else:
    print("Condition number can only be computed for a square matrix.")


# Mathematical Problem Solving Using Python

# %%
# 1. Accept an integer n.

n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("n =", n)

# %%
# 2. Compute the required sums.

if n > 0:
    # Sum of first n natural numbers
    sum_n = n * (n + 1) // 2

    # Sum of squares of first n natural numbers
    sum_squares = n * (n + 1) * (2 * n + 1) // 6

    # Sum of cubes of first n natural numbers
    sum_cubes = (n * (n + 1) // 2) ** 2

    print("\nResults")
    print(f"Sum of first {n} natural numbers        : {sum_n}")
    print(f"Sum of squares of first {n} natural numbers : {sum_squares}")
    print(f"Sum of cubes of first {n} natural numbers   : {sum_cubes}")    