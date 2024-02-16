import numpy as np

# dimension constants
O = 0
M = 0.2
L = 1.6
dn = 16001
x, dx = np.linspace(O, L, dn, retstep=True)

# material constants (Germanium)
gamma_n = 1 / 93
gamma_p = 1 / 44
ni = 2.5e13

# doping constants
Nd, Na = 1e4, 1e2
N = np.array(list(map(lambda x: Nd if x < M else -Na, x)))

# built-in potential
psi_bi = np.log(Nd * Na / (ni**2))

# border conditions
n_o, n_l = Nd, 0
p_o, p_l = 0, Na
psi_o, psi_l = 0, psi_bi
