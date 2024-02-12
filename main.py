import matplotlib.pyplot as plt
from solve import solve
from params import *
from poisson_init import *

def main():
    y = solve(dn, a, c, b, d)

    plt.figure(figsize=(10, 10))
    plt.plot(x, y)
    plt.show()

main()
