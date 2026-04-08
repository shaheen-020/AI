# Simplified hard-margin idea

import numpy as np

w = np.array([1,1])
b = -3

def predict(x):
    return 1 if np.dot(w,x)+b >= 0 else 0

print("Prediction:", predict([2,2]))