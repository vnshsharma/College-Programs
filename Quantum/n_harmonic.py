import numpy as np
import matplotlib.pyplot as plt

# Constants
hbarc = 197.3   # MeV*fm
m = 940.0       # MeV/c^2
k = 100.0       # MeV/fm^2

# Potential with anharmonic term
def V(x, b):
    return 0.5*k*x**2 + (1/3)*b*x**3

# Euler method for Schrödinger equation
def euler(E, slope, x, b):
    h = x[1]-x[0]
    psi, phi = 0.0, slope
    psi_values = [psi]
    potential = V(x, b)

    for i in range(len(x)-1):
        psi += h*phi
        phi += h*(2*m/(hbarc**2))*(potential[i]-E)*psi
        psi_values.append(psi)

    psi = np.array(psi_values)
    # normalize
    psi /= np.sqrt(np.trapz(psi**2, x))
    return psi

# Grid
N = 2000
x = np.linspace(0, 5, N+1)   # radial coordinate
slope = 1.0

# Cases
b_values = [0, 10, 30]
trial_E = [95, 100, 105]  # trial energies

# Subplots
plt.figure(figsize=(12, 8))

# First subplot for b=0
plt.subplot(3, 1, 1)
for E in trial_E:
    psi = euler(E, slope, x, b_values[0])
    plt.plot(x, psi + E/100, label=f"E={E} MeV")
plt.plot(x, V(x, b_values[0])/100, 'k--', label="V(r)/100")
plt.title("Wavefunctions for b=0 MeV/fm³")
plt.xlabel("r (fm)")
plt.ylabel("ψ(r)")
plt.legend()
plt.grid()

# Second subplot for b=10
plt.subplot(3, 1, 2)
for E in trial_E:
    psi = euler(E, slope, x, b_values[1])
    plt.plot(x, psi + E/100, label=f"E={E} MeV")
plt.plot(x, V(x, b_values[1])/100, 'k--', label="V(r)/100")
plt.title("Wavefunctions for b=10 MeV/fm³")
plt.xlabel("r (fm)")
plt.ylabel("ψ(r)")
plt.legend()
plt.grid()

# Third subplot for b=30
plt.subplot(3, 1, 3)
for E in trial_E:
    psi = euler(E, slope, x, b_values[2])
    plt.plot(x, psi + E/100, label=f"E={E} MeV")
plt.plot(x, V(x, b_values[2])/100, 'k--', label="V(r)/100")
plt.title("Wavefunctions for b=30 MeV/fm³")
plt.xlabel("r (fm)")
plt.ylabel("ψ(r)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
