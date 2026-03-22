import numpy as np

def sigmoid(x):
    x=np.array(x)
    a=1+np.exp(-x)
    return 1/a
    