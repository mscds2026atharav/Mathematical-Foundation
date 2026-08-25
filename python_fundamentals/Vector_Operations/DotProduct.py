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

print("Dot Product:", dot_product)