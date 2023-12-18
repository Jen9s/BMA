import numpy as np

epsilon = 10 ** (-5)


def Jacobi_method(A, b):
    B = np.zeros((5, 5))
    counter = 0
    for i in range(5):
        for j in range(5):
            if i != j:
                B[i][j] = -A[i][j]/A[i][i]
    print(B)

    g = np.zeros(5).transpose()
    for i in range(5):
        g[i] = b[i]/A[i][i]
    print(g)


    x_k = b
    x_k_1 = b.dot(1.2)


    while(np.linalg.norm(x_k_1 - x_k, ord=1) > epsilon) :
        print(f"\n{np.linalg.norm(x_k_1 - x_k, ord=1)} > {epsilon}\n")
        print(f"------------------iteration {counter}------------------\n")

        x_k  = x_k_1
        print(x_k)
        x_k_1 = B.dot(x_k) +g
        print(x_k_1)
        #if counter == 2 : break
        counter+=1

    print(f"\n-------------- Result ------------------\n")
    result = A.dot(x_k_1) - b
    print(f"Вектор х:{x_k_1}")
    print(f"Невязка r:{result}")
    return B
