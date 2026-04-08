#LOGISTIC REGRESSION (Formula - Sigmoid)
import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

data = ((1,0),(2,0),(3,1),(4,1))

X = np.array([i[0] for i in data])
y = np.array([i[1] for i in data])

w = 0
b = 0
lr = 0.1

for _ in range(1000):
    z = w*X + b
    y_pred = sigmoid(z)
    
    dw = np.mean((y_pred - y)*X)
    db = np.mean(y_pred - y)
    
    w -= lr*dw
    b -= lr*db

print("Prediction:", sigmoid(w*2.5 + b))