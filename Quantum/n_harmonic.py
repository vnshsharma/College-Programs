import math 
import numpy as np 
import matplotlib.pyplot as plt 
k = 100
m = 940
hcut = 197.3
b_vals = [0,10,20,30]
N = 400
x = np.linspace(-4,4,N)
h = x[1]-x[0]
omega = np.sqrt(k/m)
alpha = np.sqrt(m*omega/hcut)
coeff = (hcut**2)/(2*m*h**2)
def psi_ana(n,x,alpha):
    if n == 0:
        Hn = 1
    elif n == 1:
        Hn = 2*alpha*x
    else:
        Hn = 0
    norm = np.sqrt(alpha/(np.sqrt(np.pi)*(2**n)*math.factorial(n)))
    return norm*Hn*np.exp(-0.5*(alpha*x)**2)
num_colors = ['orange', 'green']
ana_colors = ['red', 'blue']
plt.figure(figsize=(10,8))
for idx,b in enumerate(b_vals):
    V = 0.5*k*x**2 + (1/3)*b*x**3
    H = np.zeros((N,N))
    for i in range(N):
        H[i,i] = 2*coeff + V[i]
        if i>0:
            H[i,i-1] = -coeff
        if i<N-1:
            H[i,i+1] = -coeff
    E, psi = np.linalg.eigh(H)
    psi /= np.sqrt(np.trapezoid(psi**2, x))
    plt.subplot(2,2,idx+1)
    plt.plot(x, V, color='black', label='Potential V(x)')
    # Plot both states directly without if-else
    for n in [0,1]:
        plt.plot(x, psi[:,n]**2 * 300 + E[n],color=num_colors[n], label=f'Numerical n={n}, E={E[n]:.2f}')
        plt.plot(x, psi_ana(n,x,alpha)**2 * 300 + (n+0.5)*hcut*omega, color=ana_colors[n], linestyle='--', label=f'Analytical n={n}, E={((n+0.5)*hcut*omega):.2f}')
    plt.title(f'b={b}')
    plt.xlabel('x (fm)')
    plt.ylabel('Energy')
    plt.legend(fontsize=8)
    plt.grid()
plt.suptitle("Anharmonic Oscillator", fontsize=16)
plt.tight_layout()
plt.show() 