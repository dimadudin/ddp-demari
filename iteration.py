import numpy as np
from consts import *
from util import solve_system, calculate_integral

A = np.ones(dn)
A[0], A[-1] = 0, 0

B = np.ones(dn)
B[0], B[-1] = 0, 0

def iterator():
    n = np.zeros(dn)
    p = np.zeros(dn)
    psi = np.linspace(psi_o, psi_l, dn)
    def step():
        nonlocal n
        nonlocal p
        nonlocal psi

        ijn = np.array(list(map(I_n, psi)))
        ijp = np.array(list(map(I_p, psi)))
        Jn = (n_o * np.exp(-psi_o) - n_l * np.exp(-psi_l)) / (calculate_integral(ijn, dx))
        Jp = (p_l * np.exp(psi_l) - p_o * np.exp(psi_o)) / (calculate_integral(ijp, dx))

        for i in range(dn):
            i_n = Jn * np.array(list(map(I_n, psi[i:])))
            i_p = Jp * np.array(list(map(I_p, psi[i:])))
            n[i] = np.exp(psi[i]) * (calculate_integral(i_n, dx) + n_l * np.exp(-psi_l))
            p[i] = np.exp(-psi[i]) * -(calculate_integral(i_p, dx) + p_l * np.exp(psi_l))

        c = -((dx ** 2) * (n + p) + 2)
        c[0], c[-1] = 1, 1

        d = np.zeros(dn)
        d[1:-1] = -(psi[:-2] - 2 * psi[1:-1] + psi[2:]) + (dx ** 2) * (n[1:-1] - p[1:-1] - N[1:-1])
        d[0], d[-1] = 0, 0

        delta = solve_system(dn, A, c, B, d)
        psi += delta

        return n, p, psi

    def I_n(psi):
        return gamma_n * np.exp(-psi)

    def I_p(psi):
        return gamma_p * np.exp(psi)

    return step
