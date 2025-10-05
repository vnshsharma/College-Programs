import numpy as np
import matplotlib.pyplot as plt

# Constants
hbarc = 197.3   # MeV*fm
m = 940.0       # MeV/c^2
k = 100.0       # MeV/fm^2

# Potential with anharmonic term
def V(x, b):
    return 0.5 * k * x**2 + (1/3) * b * x**3

# Schrödinger solver (Euler)
def solve_schrodinger(E, slope, x, b):
    h = x[1] - x[0]
    psi, phi = 0.0, slope
    psi_values = [psi]
    potential = V(x, b)

    for i in range(len(x) - 1):
        psi += h * phi
        phi += h * (2 * m / (hbarc**2)) * (potential[i] - E) * psi
        psi_values.append(psi)

    return np.array(psi_values)

# Automatic energy bracketing + bisection
def find_ground_state(x, b, slope=1.0, E_min=10, E_max=300, dE=2, tol=1e-3):
    # Step 1: scan energies to find sign change
    energies = np.arange(E_min, E_max, dE)
    prev_val = solve_schrodinger(energies[0], slope, x, b)[-1]

    E_low, E_high = None, None
    for E in energies[1:]:
        val = solve_schrodinger(E, slope, x, b)[-1]
        if prev_val * val < 0:  # sign change found
            E_low, E_high = E - dE, E
            break
        prev_val = val

    if E_low is None:
        raise ValueError("No eigenvalue found in scan range. Increase E_max.")

    # Step 2: bisection method
    while (E_high - E_low) > tol:
        E_mid = 0.5 * (E_low + E_high)
        psi_mid = solve_schrodinger(E_mid, slope, x, b)[-1]

        psi_low = solve_schrodinger(E_low, slope, x, b)[-1]

        if psi_low * psi_mid <= 0:
            E_high = E_mid
        else:
            E_low = E_mid

    E_ground = 0.5 * (E_low + E_high)
    psi = solve_schrodinger(E_ground, slope, x, b)

    # Normalize
    psi /= np.sqrt(np.trapezoid(psi**2, x))
    return E_ground, psi

# Grid
N = 2000
x = np.linspace(-5, 5, N+1)

# Different anharmonic strengths
b_values = [0, 10, 30, -10]

# Plot
plt.figure(figsize=(12, 10))

for idx, b in enumerate(b_values, 1):
    E, psi = find_ground_state(x, b)
    Vx = V(x, b)

    # scale ψ for visibility
    scale_factor = (max(Vx) - min(Vx)) * 0.3
    psi_scaled = psi * scale_factor + E

    plt.subplot(2, 2, idx)
    plt.plot(x, Vx, 'k--', label="Potential V(x)")
    plt.plot(x, psi_scaled, 'r', label=f"Ground ψ(x), E≈{E:.2f} MeV")

    plt.title(f"Anharmonic Oscillator (b={b} MeV/fm³)")
    plt.xlabel("x (fm)")
    plt.ylabel("Energy / ψ(x)")
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()
