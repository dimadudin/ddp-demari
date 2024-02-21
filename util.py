import numpy as np
import matplotlib.pyplot as plt
import copy
from consts import dx, dn, gamma_n, gamma_p, N


def step_ddp(n, p, psi, U):
    n_ = copy.deepcopy(n)
    p_ = copy.deepcopy(p)
    psi_ = copy.deepcopy(psi)

    Jn, Jp = get_currents(n, p, psi, U)
    n_, p_ = get_densities(n[-1], p[-1], psi, Jn, Jp)
    psi_ = solve_poisson(n_, p_, psi)

    return n_, p_, psi_, Jn, Jp


def solve_poisson(n, p, psi):
    d1 = np.ones(dn)
    d1[0], d1[-1] = 0, 0
    d0 = np.array(-((dx**2) * (n + p) + 2))
    d0[0], d0[-1] = 1, 1

    rhs = np.zeros(dn)
    rhs[1:-1] = -(psi[:-2] - 2 * psi[1:-1] + psi[2:]) + (dx**2) * (
        n[1:-1] - p[1:-1] - N[1:-1]
    )
    rhs[0], rhs[-1] = 0, 0

    dpsi = np.array(solve_tridiag(d1, d0, d1, rhs))
    return psi + dpsi


def get_currents(n, p, psi, U):
    IU = np.array([calc_I(U[: i + 1], dx) for i in range(dn)])

    exp_neg = np.exp(-psi)
    In1 = calc_I(gamma_n * exp_neg, dx)
    In2 = calc_I(gamma_n * exp_neg * IU, dx)
    Jn = -IU + (n[0] * exp_neg[0] - n[-1] * exp_neg[-1] + In2) / In1

    exp_pos = np.exp(psi)
    Ip1 = calc_I(gamma_p * exp_pos, dx)
    Ip2 = calc_I(gamma_p * exp_pos * IU, dx)
    Jp = IU + (p[-1] * exp_pos[-1] - p[0] * exp_pos[0] - Ip2) / Ip1

    return Jn, Jp


def get_densities(nL, pL, psi, Jn, Jp):
    exp_pos = np.exp(psi)
    exp_neg = np.exp(-psi)

    In = np.array([calc_I(gamma_n * Jn[i:] * exp_neg[i:], dx) for i in range(dn)])
    n_ = exp_pos * (In + nL * exp_neg[-1])

    Ip = np.array([calc_I(gamma_p * Jp[i:] * exp_pos[i:], dx) for i in range(dn)])
    p_ = exp_neg * (-Ip + pL * exp_pos[-1])

    return n_, p_


def solve_tridiag(low, mid, up, rhs):
    a = copy.deepcopy(low)
    c = copy.deepcopy(mid)
    b = copy.deepcopy(up)
    d = copy.deepcopy(rhs)
    n = len(c)
    b[0] /= c[0]
    d[0] /= c[0]
    for i in range(1, n):
        fac = c[i] - a[i] * b[i - 1]
        b[i] /= fac
        d[i] = (d[i] - a[i] * d[i - 1]) / fac
    y = [0] * n
    y[-1] = d[-1]
    for i in range(n - 2, -1, -1):
        y[i] = d[i] - b[i] * y[i + 1]
    return y


def calc_I(y, dx):
    return dx / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])


def plot(x, y, y_label, fname):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel(y_label)
    plt.grid(True)
    plt.savefig(fname)
    plt.close()
