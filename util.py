import numpy as np

def sys_solve(dn, a, c, b, d):
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

def i_calc(y, dx):
    return dx/3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])