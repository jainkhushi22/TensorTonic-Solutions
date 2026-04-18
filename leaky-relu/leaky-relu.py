import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    a=np.array(x)
    return np.maximum(alpha*a , a)