import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 940e6     # eV/(c^2)
De = 4.75     # eV
a = 1.94      # A^(-1)
hcut = 1973   # eV A/c
re = 0.74     # A
N = 1000
L = 1
k = 100
r = np.linspace(re - L, re + L, N)
h = r[1] - r[0]

# Potentials
def harmonic_potential(r):
    return 0.5 * k * (r - re)**2

def morse_potential(r):
    V = De * (np.exp(-2 * a * (r - re)) - 2 * np.exp(-a * (r - re)))
    return V + De  

V_harmonic = harmonic_potential(r)
V_morse = morse_potential(r)

# Hamiltonian for Morse potential
H_morse = np.zeros((N, N))
coeff = (hcut ** 2) / (2 * m * h ** 2)
for i in range(N):
    H_morse[i, i] = 2 * coeff + V_morse[i]
    if i > 0:
        H_morse[i, i - 1] = -coeff
    if i < N - 1:
        H_morse[i, i + 1] = -coeff
E_morse, psi_morse = np.linalg.eigh(H_morse)

# Hamiltonian for Harmonic potential
H_harm = np.zeros((N, N))
for i in range(N):
    H_harm[i, i] = 2 * coeff + V_harmonic[i]
    if i > 0:
        H_harm[i, i - 1] = -coeff
    if i < N - 1:
        H_harm[i, i + 1] = -coeff
E_harm, psi_harm = np.linalg.eigh(H_harm)

# States 
states = [0, 1, 2, 10]

plt.figure(figsize=(10, 8))
for idx, n in enumerate(states):
    # Morse wavefunction
    wf = psi_morse[:, n]
    P_morse = wf ** 2
    P_morse /= np.trapezoid(P_morse, r)
    scale_morse = De / (2 * np.max(P_morse))
    P_morse_scaled = P_morse * scale_morse
    E_level_morse = E_morse[n]

    # Harmonic wavefunction
    wf_h = psi_harm[:, n]
    P_harm = wf_h ** 2
    P_harm /= np.trapezoid(P_harm, r)
    scale_harm = De / (2 * np.max(P_harm))
    P_harm_scaled = P_harm * scale_harm
    E_level_harm = E_harm[n]

    plt.subplot(2, 2, idx + 1)
    # plt.fill_between(r, E_level_morse, P_morse_scaled + E_level_morse, color='blue', alpha=0.3, label='Morse |ψ|²')
    plt.plot(r, P_morse_scaled + E_level_morse, color='b',label='Morse |ψ|²')
    plt.plot(r, P_harm_scaled + E_level_harm, color='green', label='Harmonic |ψ|²')

    plt.plot(r, V_morse, 'k--', label='Morse Potential')
    plt.plot(r, V_harmonic, color='grey', linestyle='--', label='Harmonic Potential')
    plt.axhline(De, color='r', linestyle='--', label='Dissociation Energy')

    plt.xlabel('r (Å)')
    plt.ylabel('Energy (eV)')
    plt.title(f'for n={n}', fontsize=14)
    plt.grid()
    plt.legend()
    plt.ylim(-0.2, 10)

plt.suptitle("Morse Potential", fontsize=20)
plt.tight_layout()
plt.show()

# Print energy levels
print("Vibrational energy levels (in eV):")
for n in states:
    print(f'n={n}: Morse E={E_morse[n]:.2f}, Harmonic E={E_harm[n]:.2f}')
print(f'Near Dissociation: Morse E={E_morse[-1]:.2f} eV') 

mu = m / 2      # reduced mass of H2 in eV/(c^2) 
print(f"Reduced mass of H2: {mu:.2e} eV/c^2") 