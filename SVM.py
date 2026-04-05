# weights
w = [1, -1]
b = 0

# input
x = [2, 3]

# dot product
result = w[0]*x[0] + w[1]*x[1] + b

if result >= 0:
    print("Class 1")
else:
    print("Class 0")
