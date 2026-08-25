epsilon = 1.0

while 1.0 + epsilon != 1.0:
    epsilon /= 2

epsilon *= 2

print("Machine Epsilon for float =", epsilon)