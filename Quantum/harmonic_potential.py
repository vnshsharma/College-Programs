import numpy as np
import matplotlib.pyplot as plt

# Potential function for a quantum harmonic oscillator
def V(x, k=10):
    # The potential energy for a harmonic oscillator is 1/2 * k * x^2
    return 0.5 * k * x**2

# Euler method to solve for the wavefunction
def euler(E, slope, x):
    h = x[1] - x[0]
    psi, phi = 0, slope
    psi_values = [psi]
    potential = V(x)
    for i in range(len(x) - 1):
        psi += h * phi
        phi += h * (2 * (potential[i] - E) * psi)
        psi_values.append(psi)
    return np.array(psi_values)

# Plotting function
def plot_wavefunction(E):
    N = 1000
    x = np.linspace(-3, 3, N + 1)
    psi = euler(E, 1, x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, psi, label='Wavefunction')
    plt.plot(x, V(x) / 10, 'k--', label='Potential/10')
    plt.grid(True)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('ψ(x)')
    plt.title(f'Quantum Harmonic Oscillator (E = {E:.1f})')
    plt.show()

# Main execution block
if __name__ == "__main__":
    plot_wavefunction(0.5)
