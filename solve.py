import numpy as np

def solve(dn, a, c, b, d):
    alpha = np.zeros(dn)
    beta = np.zeros(dn)

    alpha[0] = -b[0] / c[0]
    beta[0] = d[0] / c[0]

    for i in range (1, dn):
        alpha[i] = (-b[i] / (a[i] * alpha[i-1] + c[i]))
        beta[i] = ((d[i] - a[i] * beta[i-1]) / (a[i] * alpha[i-1] + c[i]))

    y = np.zeros(dn)
    y[-1] = beta[-1]

    for i in range (dn-1, -1, -1):
        y[i-1] = alpha[i-1] * y[i] + beta[i-1]

    return y
