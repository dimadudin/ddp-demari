import numpy as np
from consts import x, dn, psi_o, psi_l, Nd, Na, M
from util import step_ddp, plot

n = np.array(list(map(lambda x: Nd if x < M else 0, x)))
p = np.array(list(map(lambda x: 0 if x < M else Na, x)))
psi = np.linspace(psi_o, psi_l, dn)
U = np.zeros(dn)

print("initial:")
print(f"n(O): {n[0]}, n(L): {n[-1]}")
plot(x, n, "n")

print(f"p(O): {p[0]}, p(L): {p[-1]}")
plot(x, p, "p")

print(f"psi(O): {psi[0]}, psi(L): {psi[-1]}")
plot(x, psi, "psi")


for i in range(50):
    print(f"iteration: {i+1}")
    n_, p_, psi_, Jn, Jp = step_ddp(n, p, psi, U)
    n, p, psi = n_, p_, psi_
    print(f"n(O): {n_[0]}, n(L): {n_[-1]}")
    print(f"p(O): {p_[0]}, p(L): {p_[-1]}")
    print(f"psi(O): {psi_[0]}, psi(L): {psi_[-1]}")
    print(f"Jn: {Jn[0]}, Jp: {Jp[0]}")

plot(x, n, "n_")
plot(x, p, "p_")
plot(x, psi, "psi_")
