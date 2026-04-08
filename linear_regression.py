# Data
X = [1, 2, 3, 4]
y = [5, 6, 7, 8]

n = len(X)

# Mean
mean_x = sum(X) / n
mean_y = sum(y) / n

# Calculate slope (m)

num = sum((X[i] - mean_x) * (y[i] - mean_y) for i in range(n))
den = sum((X[i] - mean_x) ** 2 for i in range(n))

m = num / den

# Intercept (c)
c = mean_y - m * mean_x

# Output equation
print("Equation: y =", m, "x +", c)

# Prediction
x_new = 5
y_pred = m * x_new + c

print("Prediction:", y_pred)
