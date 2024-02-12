from params import *
import numpy as np

a = np.zeros(dn)
a[0] = 0
a[1:dn] = np.ones(dn - 1)
a[-1] = 0

c = np.zeros(dn)
c[0] = 1
c[1:dn] = -2 * np.ones(dn - 1)
c[-1] = 1

b = np.zeros(dn)
b[0] = 0
b[1:dn] = np.ones(dn - 1)
b[-1] = 0

d = np.zeros(dn)
d[0] = (dx ** 2) * psi_o
d[1:dn] = (dx ** 2) * (n[1:dn] - p[1:dn] - N[1:dn])
d[-1] = (dx ** 2) * psi_l
