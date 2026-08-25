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

print("Euclidean Norm of Vector 1:", norm1)
print("Euclidean Norm of Vector 2:", norm2)