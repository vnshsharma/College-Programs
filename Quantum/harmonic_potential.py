import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 300
x_min, x_max = -5, 5
x = np.linspace(x_min, x_max, N)
h = x[1] - x[0]
m = 940.0     # mass
k = 100.0     # spring constant
hcut = 197.3  # ħ (MeV·fm)

# Hamiltonian Matrix
A = np.zeros((N, N))
for i in range(N):
    A[i][i] = -2
    if i > 0:
        A[i][i - 1] = 1
    if i < N - 1:
        A[i][i + 1] = 1

# Kinetic energy operator scaling
for i in range(N):
    for j in range(N):
        A[i][j] = -(hcut**2) * A[i][j] / (2 * m * h**2)

# Add potential energy
for i in range(N):
    Vx = 0.5 * k * x[i]**2
    A[i][i] += Vx

# Solve eigenvalue problem
E, psi = np.linalg.eigh(A)

# Normalize eigenfunctions using loops
for n in range(len(E)):
    sq_vals = []
    for j in range(N):
        sq_vals.append(psi[j][n]**2)
    norm = np.sqrt(np.trapezoid(sq_vals, x))
    for j in range(N):
        psi[j][n] /= norm
    if psi[0][n] < 0:  # flip sign for consistency
        for j in range(N):
            psi[j][n] = -psi[j][n]

# Plot potential
plt.plot(x, 0.5 * k * x**2, 'k--', label="Potential V(x)")

# Plot selected eigenstates with better scaling
levels = [0, 1, 2, 20]
scale_factor = 10.0  # makes wavefunction curves more visible
for n in levels:
    y = []
    for j in range(N):
        y.append(scale_factor * psi[j][n] + E[n])  
    plt.plot(x, y, label=f'n={n}, E={E[n]:.2f}')

plt.xlabel("x")
plt.ylabel("Energy / ψ(x)")
plt.title("Quantum Harmonic Oscillator (Numerical)")
plt.legend()
plt.grid()
plt.show()
