import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    s=np.maximum(0,x)
    return s