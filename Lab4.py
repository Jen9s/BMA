import numpy as np

y_k = np.array([1, 2, 3])
y_k_1 = np.array([4, 5, 6])

scalar_product = np.dot(y_k, y_k_1)

print("Скалярное произведение:", scalar_product)

def method_Krylov(matrix):
    A = matrix*matrix.T

    

    return A