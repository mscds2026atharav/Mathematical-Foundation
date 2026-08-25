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

print("Element-wise Multiplication:", result)