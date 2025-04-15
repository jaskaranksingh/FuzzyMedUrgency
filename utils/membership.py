
import numpy as np

def sigmoid(x, k=1):
    return 1 / (1 + np.exp(-k * x))

def stupa_membership(x, a, b, stiffness=5):
    x = np.array(x)
    left = sigmoid(-(x - a) * stiffness / (b - a))
    right = sigmoid((x - b) * stiffness / (b - a))
    return np.minimum(left, right)
