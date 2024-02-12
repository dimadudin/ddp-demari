import numpy as np
O = 0
M = 0.2
L = 1.6

dn = 161

x, dx = np.linspace(O, L, dn, retstep=True)

M_i, = np.where(x == M)[0]

Nd = 1e4
Na = 1e2
ni = 2.5e13

N = np.zeros(dn)

N[:M_i] = [Nd for _ in range(M_i)]
N[M_i:] = [-Na for _ in range(dn-M_i)]

n = np.zeros(dn)
n[:M_i] = [Nd for _ in range(M_i)]
n[M_i:] = [0 for _ in range(dn-M_i)]

p = np.zeros(dn)
p[:M_i] = [0 for _ in range(M_i)]
p[M_i:] = [Na for _ in range(dn-M_i)]

psi_bi = np.log(Nd * Na / (ni ** 2))
psi_o = psi_bi
psi_l = 0
