import numpy as np


def nevilleMethod(x, y, w):
    n = len(x)
    m = len(y)

    neville = np.zeros((n, m))

    for i in range(m):
        neville[i][0] = y[i]

    for i in range(1, n):
        for j in range(1, m):
            term1 = (w - x[i - j]) * neville[i][j - 1]
            term2 = (w - x[i]) * neville[i - 1][j - 1]
            neville[i][j] = (term1 - term2) / (x[i] - x[i - j])

    return neville[n - 1][m - 1]


def newtons(x, y):
    n = len(x)
    
    diffs = np.zeros((n, n))

    for i in range(n):
        diffs[i][0] = y[i]

    for i in range(1, n):
        for j in range(1, i+1):
            diffs[i][j] = (diffs[i][j - 1] - diffs[i - 1][j - 1]) / (x[i] - x[i - j])


    return diffs


def newton_interpolate(x, diffs, x_eval):

    n = len(x)

    result = diffs[0][0]

    product_term = 1.0

    for i in range(1, n):
        product_term *= (x_eval - x[i-1])

        result += diffs[i][i] * product_term

    return result


def hermite_polynomial(x, y, yp):
    n = len(x)
    m = 2 * n

    Q = np.zeros((m, m-1))

    for i in range(m):
        Q[i][0] = x[i//2]
        Q[i][1] = y[i//2]

    for i in range(m):
        if i == 0:
            Q[i][2] = 0.0
        elif i % 2 == 1:
            Q[i][2] = yp[i//2]
        else:
            Q[i][2] = (Q[i][1] - Q[i - 1][1]) / (Q[i][0] - Q[i - 1][0])


    for i in range(2, m):
        for j in range(2, i+2):
            if j >= len(Q[i]) or Q[i][j] != 0:
                continue
            Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1]) / (Q[i][0] - Q[i - j+1][0])


    return Q


def cubic_spline(x, y):

    n = len(x)
    A = np.zeros((n, n))

    h = np.diff(x)

    A[0][0] = 1
    A[n-1][n-1] = 1
    for i in range(1, n-1):
        A[i][i-1] = h[i-1]
        A[i][i] = 2 * (h[i-1] + h[i])
        A[i][i+1] = h[i]

    b = np.zeros(n)

    for i in range(1, n-1):
        b[i] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])

    x = np.linalg.solve(A, b)   

    return A, b, x