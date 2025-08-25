import numpy as np
import matplotlib.pyplot as plt

def solve(E, slope, N=1000):
    h = 1 / N
    psi, phi = 0.0, slope
    values = [psi]
    for i in range(N):
        k1psi, k1phi = h * phi, h * (-2 * E * psi)
        k2psi, k2phi = h * (phi + k1phi / 2), h * (-2 * E * (psi + k1psi / 2))
        k3psi, k3phi = h * (phi + k2phi / 2), h * (-2 * E * (psi + k2psi / 2))
        k4psi, k4phi = h * (phi + k3phi), h * (-2 * E * (psi + k3psi))
        psi += (k1psi + 2 * k2psi + 2 * k3psi + k4psi) / 6
        phi += (k1phi + 2 * k2phi + 2 * k3phi + k4phi) / 6
        values.append(psi)
    return np.array(values)

def psi_exact(x, n=1):
    return np.sqrt(2) * np.sin(n * np.pi * x)

# Define domain outside
N = 1000
x = np.linspace(0, 1, N + 1)

# Trial energies
for E in [4.0, 9.0, 16.0]:
    psi = solve(E, slope=1.0, N=N)
    plt.plot(x, psi, label=f"Trial E={E}")

# Eigenvalue solution (n=1)
n = 1
E_n = (n * np.pi) ** 2 / 2
slope = np.sqrt(2) * n * np.pi
psi_num = solve(E_n, slope, N)
plt.plot(x, psi_num, "r", label=f"E_n={E_n:.4f} (eigenvalue)")

# Analytical
plt.plot(x, psi_exact(x, n), "k--", label=f"Analytical n={n}")

plt.title("Infinite Well ψ(x): Trial vs Eigenvalue")
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.legend()
plt.grid()
plt.show()
