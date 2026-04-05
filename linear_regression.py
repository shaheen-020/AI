X = [1, 2, 3, 4]
y = [2, 4, 6, 8]

n = len(X)

mean_x = sum(X) / n
mean_y = sum(y) / n

num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

m = num / den
c = mean_y - m * mean_x

print("m =", m)
print("c =", c)

# prediction
x_new = 5
y_pred = m * x_new + c
print("Prediction:", y_pred)
