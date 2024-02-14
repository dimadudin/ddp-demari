from consts import x
import iteration as it
import matplotlib.pyplot as plt

def main():
    step = it.iterator()
    n, p, psi = step()

    plt.figure(figsize=(10, 10))
    plt.plot(x, n)
    plt.show()

    plt.figure(figsize=(10, 10))
    plt.plot(x, p)
    plt.show()

    plt.figure(figsize=(10, 10))
    plt.plot(x, psi)
    plt.show()

main()
