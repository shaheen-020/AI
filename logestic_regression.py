import math

# weights
w = 1
b = -3

x = 4

z = w * x + b
prob = 1 / (1 + math.exp(-z))

print("Probability:", prob)

# classification
if prob >= 0.5:
    print("Class: 1")
else:
    print("Class: 0")
