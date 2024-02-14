from consts import x
import iteration as it
from util import save_plot

def main():
    for i in range(20):
        step = it.iterator()
        n, p, psi = step()

        save_plot(x, n, 'n', f"res/electron_densities/n_{i}.png")
        save_plot(x, p, 'p', f"res/hole_densities/p_{i}.png")
        save_plot(x, psi, 'psi', f"res/potential/psi_{i}.png")

main()
