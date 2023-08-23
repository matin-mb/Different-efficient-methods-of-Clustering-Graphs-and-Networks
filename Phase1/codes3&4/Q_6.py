from math import log
import numpy as np


def calculate(matrix, Z, Q):
    l_z = 0
    n = len(Z)
    for i in range(n):
        for j in range(i + 1, n):
            a = Z[i] - 1
            b = Z[j] - 1
            q = Q[a, b]
            l_z += log(1 + 2 * matrix[i][j] * q - q - matrix[i][j])
    return l_z


def l_tilda(matrix, Z):
    p = 0.6
    q = 0.1
    n = len(Z)
    Q = np.eye(n) * (p - q) + np.ones(n) * q

    l_z = calculate(matrix, Z, Q)

    lTilda = -l_z
    return lTilda


z = [3, 1, 2, 1, 3, 1, 2, 2, 2, 3, 3, 2, 1, 1, 3]
A = [[0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 1.],
     [0., 0., 0., 0., 0., 1., 0., 0., 0., 1., 1., 0., 0., 1., 0.],
     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
     [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0.],
     [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
     [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0.],
     [0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1.],
     [0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 1., 1., 0., 0.],
     [0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 0.],
     [0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
     [1., 1., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 1.],
     [0., 0., 1., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0.],
     [0., 0., 0., 1., 0., 1., 0., 1., 0., 0., 0., 0., 0., 1., 0.],
     [0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
     [1., 0., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0.]]


# z = list(map(int, input().split()))
# A = list(map(int, input().split()))

l_tilda = l_tilda(A, z)
print("l_tilda(z) = " + str(l_tilda))
