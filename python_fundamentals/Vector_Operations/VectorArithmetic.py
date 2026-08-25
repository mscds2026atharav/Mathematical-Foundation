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

print("Vector Addition:", addition)
print("Vector Subtraction:", subtraction)