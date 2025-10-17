import math
import numpy as np
import matplotlib.pyplot as plt

N = 400
k = 100
m = 940
hcut = 197.3
x = np.linspace(-4, 4, N)
h = x[1] - x[0]
b_val = [0, 10, 30]
omega = np.sqrt(k/m)

# --- Hamiltonian ---
def hamiltonian(b):
    V = 0.5*k*x**2 + (1/3)*b*x**3
    H = np.zeros((N, N))
    coeff = (hcut**2)/(m*h**2)
    for i in range(N):
        H[i,i] = coeff + V[i]
        if i > 0:
            H[i,i-1] = -0.5*coeff
        if i < N-1:
            H[i,i+1] = -0.5*coeff
    return H, V

# --- Analytical Wavefunction ---
alpha = np.sqrt(m*omega/hcut)
def psi_analytical(n, x, alpha):
    if n == 0:
        Hn = 1
    elif n == 1:
        Hn = 2*alpha*x
    elif n == 2:
        Hn = 4*(alpha*x)**2 - 2
    else:
        Hn = 0
    norm = np.sqrt(alpha/(np.sqrt(np.pi)*2**n*math.factorial(n)))
    return norm*Hn*np.exp(-0.5*(alpha*x)**2)

# --- Analytical Energy ---
def energy_analytical(n):
    return hcut*omega*(n + 0.5)

# Harmonic potential for reference (b = 0)
V_harmonic = 0.5*k*x**2

# States to plot
states = [0, 1, 2]

plt.figure(figsize=(14, 10))

for row, n in enumerate(states):
    wf_ana = psi_analytical(n, x, alpha)
    P_ana = wf_ana**2
    P_ana /= np.trapezoid(P_ana, x)
    E_ana = energy_analytical(n)
    
    for col, b in enumerate(b_val):
        H, V = hamiltonian(b)
        E, psi = np.linalg.eigh(H)
        
        P_num = psi[:,n]**2
        P_num /= np.trapezoid(P_num, x)
        
        P_num_new = P_num*300 + min(V)
        P_ana_new = P_ana*300 + min(V)
        
        plt.subplot(len(states), len(b_val), row*len(b_val)+col+1)
        plt.fill_between(x, min(V), P_num_new, color='blue', alpha=0.3)
        
        # Plot actual potentials
        plt.plot(x, V, 'k--', label='Anharmonic Potential')
        plt.plot(x, V_harmonic, 'g--', label='Harmonic Potential')
        
        # Plot analytical and numerical wavefunctions
        plt.plot(x, P_ana_new, 'r', label=f'Analytical |ψ|², E={E_ana:.2f}')
        plt.plot(x, P_num_new, 'b--', label=f'Numerical |ψ|², E={E[n]:.2f}')
        
        plt.xlabel('x')
        plt.ylabel('Prob. Density')
        plt.title(f'n={n}, b={b}')
        plt.grid()
        plt.legend(fontsize=7)

plt.tight_layout()
plt.show()
