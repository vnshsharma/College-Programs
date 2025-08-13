import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 1.0       # box length
n = 1         # quantum number
k = n * np.pi / a
h = 0.01      # step size
steps = int(a / h) + 1

# Arrays
x = np.zeros(steps)
psi = np.zeros(steps)
phi = np.zeros(steps)

# Initial conditions
psi[0] = 0.0   # psi(0) = 0
phi[0] = 1.0   # initial slope

# Euler's method loop
for i in range(steps - 1):
    psi[i+1] = psi[i] + h * phi[i]
    phi[i+1] = phi[i] - h * (k**2) * psi[i]
    x[i+1] = x[i] + h

# Plot
plt.plot(x, psi)
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.title("Schrödinger Equation - Particle in a Box")
plt.grid(True)
plt.show()