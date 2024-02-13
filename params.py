import numpy as np

# dimension constants
O = 0
M = 0.2
L = 1.6
dn = 161
x, dx = np.linspace(O, L, dn, retstep=True)
M_i, = np.where(x == M)[0]

# carrier mobilites (the inverse of them rather)
gamma_n = 1 / 93
gamma_p = 1 / 44

# doping constants
Nd = 1e4
Na = 1e2
ni = 2.5e13

N = np.zeros(dn)
N[:M_i] = [Nd for _ in range(M_i)]
N[M_i:] = [-Na for _ in range(dn-M_i)]

# carrier densities
n = np.zeros(dn)
n[:M_i] = np.array([Nd for _ in range(M_i)])
n[M_i:] = np.array([0 for _ in range(dn-M_i)])

n_o = Nd
n_l = 0

p = np.zeros(dn)
p[:M_i] = np.array([0 for _ in range(M_i)])
p[M_i:] = np.array([Na for _ in range(dn-M_i)])

p_o = 0
p_l = Na

# electric potential
psi = np.zeros(dn)

psi_bi = np.log(Nd * Na / (ni ** 2))
psi_o = psi_bi
psi_l = 0

# current densities
Jn = np.zeros(dn)
Jp = np.zeros(dn)
