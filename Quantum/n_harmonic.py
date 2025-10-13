import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

# =====================================================
#                Physical Parameters
# =====================================================
m = 940.0                     # MeV/c^2
k = 100.0                     # MeV/fm^2
b_values = [0.0, 10.0, 30.0]   # MeV/fm^3
hbar_c = 197.3                # MeV*fm

# =====================================================
#                Numerical Parameters
# =====================================================
x_min, x_max = -8.0, 8.0      # Position range (fm)
N = 500                       # Grid points
x = np.linspace(x_min, x_max, N)
dx = x[1] - x[0]

# =====================================================
#                Kinetic Energy Matrix
# =====================================================
factor = (hbar_c**2) / (2 * m * dx**2)
main_diag = np.full(N, 2 * factor)
off_diag = np.full(N - 1, -factor)
T_sparse = diags([off_diag, main_diag, off_diag], offsets=[-1, 0, 1], format='csr')

# =====================================================
#      Function to Solve for Ground State Energy
# =====================================================
def solve_ground_state(b):
    """Solve the ground state energy and wavefunction for a given b value."""
    # Potential: V(x) = 1/2 k x^2 + 1/3 b x^3
    V = 0.5 * k * x**2 + (1.0 / 3.0) * b * x**3
    V_matrix = diags(V, 0, format='csr')

    # Hamiltonian
    H = T_sparse + V_matrix

    # Solve for the lowest eigenvalue and eigenvector
    energies, wavefuncs = eigsh(H, k=1, which='SA')
    E0 = energies[0]
    psi0 = wavefuncs[:, 0]

    # Normalize wavefunction
    norm = np.sqrt(np.trapz(psi0**2, x))
    psi0 /= norm

    return E0, psi0, V

# =====================================================
#                Plotting with Subplots
# =====================================================
fig, axes = plt.subplots(1, len(b_values), figsize=(18, 6), sharey=True)
fig.suptitle("Anharmonic Oscillator — Ground State Energy & Wavefunction", fontsize=14, fontweight='bold')

for i, b in enumerate(b_values):
    # Solve Schrödinger equation
    E0, psi0, V = solve_ground_state(b)

    # Adaptive scaling for better visualization
    scale_factor = (np.max(V) - np.min(V)) * 0.25

    ax = axes[i]
    ax.plot(x, V, 'r--', label="Potential V(x)")
    ax.plot(x, psi0 * scale_factor + E0, 'b', label="Ground State ψ₀(x)")

    # Fill under the wavefunction for clarity
    ax.fill_between(x, E0, psi0 * scale_factor + E0, color='blue', alpha=0.2)

    # Plot details
    ax.set_title(f"b = {b} MeV/fm³\nE₀ = {E0:.3f} MeV", fontsize=11)
    ax.set_xlabel("x (fm)")
    if i == 0:
        ax.set_ylabel("Energy / Wavefunction (MeV)")
    ax.grid(True)
    ax.legend(fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
