import math
import numpy as np
import matplotlib.pyplot as plt

N = 400
k = 100
m = 940
hcut = 197.3
x = np.linspace(-4, 4, N)
h = x[1] - x[0]

# Potential Energy
V = np.zeros(N)
for i in range(N):
    V[i] = 0.5 * k * x[i]**2

# Hamiltonian Matrix
H = np.zeros((N, N))
for i in range(N):
    H[i][i] = (hcut**2)/(m*h**2) + V[i]
    if i > 0:
        H[i][i-1] = -0.5 * (hcut**2)/(m*h**2)
    if i < N-1:
        H[i][i+1] = -0.5 * (hcut**2)/(m*h**2)
E, psi = np.linalg.eigh(H)

# Normalization Numerical Solution
for n in range(psi.shape[1]):
    norm = 0
    for i in range(N):
        norm += psi[i][n]**2 * h
    for i in range(N):
        psi[i][n] /= np.sqrt(norm)

def get_wavefunction(psi_matrix, N, column):
    wf = np.zeros(N)
    for i in range(N):
        wf[i] = psi_matrix[i][column]
    return wf

alpha = np.sqrt(m * k) / hcut

def psi_analytical(n, x, alpha):
    if n == 0:
        Hn = 1
    elif n == 1:
        Hn = 2 * alpha * x
    elif n == 2:
        Hn = 4 * (alpha*x)**2 - 2
    else:
        Hn = 0  
    norm = np.sqrt(alpha / (np.sqrt(np.pi) * 2**n * math.factorial(n)))
    return norm * Hn * np.exp(-0.5 * (alpha*x)**2)

# --- Plot ---
plt.figure(figsize=(10,8))

# Numerical vs Analytical for n = 0,1,2
for i in range(3):
    plt.subplot(2, 2, i+1)
    wf = get_wavefunction(psi, N, i)
    plt.plot(x, wf, label='Numerical')
    plt.plot(x, psi_analytical(i, x, alpha), '--k', label='Analytical')
    plt.title(f'For n={i}')
    plt.legend()
    plt.grid()

# n = 20 
plt.subplot(2, 2, 4)
wf20 = get_wavefunction(psi, N, 20)
plt.plot(x, wf20, label='Numerical')
plt.title('For n=20')
plt.legend()
plt.grid()

plt.suptitle('Harmonic Oscillator')
plt.tight_layout()
plt.show()
