import numpy as np

def hermite_polynomial(x, y, yp):
    n = len(x)
    m = 2 * n

    Q = np.zeros((m, m))

    for i in range(n):
        Q[x] = x[i // 2]
        
    for i in range(n):
        if i == 0:
            Q[i][2] = 0.0

        elif x%2 == 1:
            Q[i][2] = yp[i // 2]

        else:
            Q[i][2] = (Q[i][1] - Q[i - 1][1]) / (Q[i][0] - Q[i - 1][0])