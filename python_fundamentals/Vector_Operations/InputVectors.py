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