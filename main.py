import matplotlib.pyplot as plt
from util import sys_solve, i_calc
from params import *
from poisson_init import *

def main():
    psi = sys_solve(dn, a, c, b, d)

    plt.figure(figsize=(10, 10))
    plt.plot(x, psi)
    plt.show()

    i1 = np.array([np.exp(-psi[i]) for i in range(dn)])
    i2 = np.array([np.exp(psi[i]) for i in range(dn)])

    Jn = (n_o * np.exp(-psi_o) - n_l * np.exp(-psi_l)) / (gamma_n * i_calc(i1, dx))
    Jp = (p_l * np.exp(psi_l) - p_o * np.exp(psi_o)) / (gamma_p * i_calc(i2, dx))

    print(Jn)
    print(Jp)

    n = [np.exp(psi[i]) * (gamma_n * Jn * i_calc(i1[i:], dx) + n_l * np.exp(-psi_l)) for i in range(dn)]
    p = [np.exp(-psi[i]) * -(gamma_p * Jp * i_calc(i2[i:], dx) + p_l * np.exp(psi_l)) for i in range(dn)]

    plt.figure(figsize=(10, 10))
    plt.plot(x, n)
    plt.show()

    plt.figure(figsize=(10, 10))
    plt.plot(x, p)
    plt.show()

main()
