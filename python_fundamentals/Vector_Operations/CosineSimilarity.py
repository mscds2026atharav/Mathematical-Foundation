# Compute Cosine Similarity between two vectors

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

print("Euclidean norm of vector 1: ",norm1)
print("Euclidean norm of vector 2: ",norm2)

# Cosine similarity
cosine_similarity = dot_product / (norm1 * norm2)

print("Cosine Similarity:", cosine_similarity)