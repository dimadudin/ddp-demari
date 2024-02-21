import numpy as np

from consts import x, dn, psi_o, psi_l, Nd, Na, M, Vt
from util import step_ddp, plot

n = np.array(list(map(lambda x: Nd if x < M else 0, x)))
p = np.array(list(map(lambda x: 0 if x < M else Na, x)))
psi = np.linspace(psi_o, psi_l, dn)
U = np.zeros(dn)

print("initial:")
print(f"n(O): {n[0]}, n(L): {n[-1]}")
print(f"p(O): {p[0]}, p(L): {p[-1]}")
print(f"psi(O): {psi[0]}, psi(L): {psi[-1]}")

plot(x, n, "n", "res/n_0.png")
plot(x, p, "p", "res/p_0.png")
plot(x, Vt * psi, "psi", "res/psi_0.png")

error = 1
tolerance = 1e-3
i = 0
max_it = 50
while error >= tolerance and i < max_it:
    print(f"iteration: {i+1}")
    n_, p_, psi_, Jn, Jp = step_ddp(n, p, psi, U)
    error = np.linalg.norm(psi_ - psi)
    n, p, psi = n_, p_, psi_
    print(f"error: {error}")
    print(f"n(O): {n[0]}, n(L): {n[-1]}")
    print(f"p(O): {p[0]}, p(L): {p[-1]}")
    print(f"psi(O): {psi[0]}, psi(L): {psi[-1]}")
    print(f"Jn: {Jn[0]}, Jp: {Jp[0]}")
    i += 1

plot(x, n, "n", f"res/n_{i}.png")
plot(x, p, "p", f"res/p_{i}.png")
plot(x, Vt * psi, "psi", f"res/psi_{i}.png")
