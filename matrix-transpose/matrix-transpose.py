import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    lst1=np.zeros(np.shape(A)[::-1])
    for i in range(lst1.shape[0]):
        for j in range(lst1.shape[1]):
            lst1[i][j]=A[j][i]

    return lst1

        
                                                
