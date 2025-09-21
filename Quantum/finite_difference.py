import numpy as np 
import matplotlib.pyplot as plt
N = 200
h = 1/N
x = np.linspace(0,1,N)
# Hamiltonian matrix 
A = np.zeros((N,N))
for i in range(N):
    A[i][i] = -2
    if i>0:
        A[i][i-1] = 1
    if i<N-1:
        A[i][i+1] = 1
A = -A/(2*h**2)
# Eigenvalues and Eigenstates
E,psi = np.linalg.eigh(A)
plt.figure(figsize=(14,8))
for i in range(N):
    if psi[0][i]<0:
        for j in range(N):
            psi[j][i] = -psi[j][i]
    sq_vals = []
    for j in range(N):
        sq_vals.append(psi[j][i]**2)
    norm = np.sqrt(np.trapezoid(sq_vals,x))
    for j in range(N):
        psi[j][i] /= norm
for i in range(3):
    plt.subplot(3,1,(i+1))
    psi_exact = np.sqrt(2)*np.sin(np.pi*(i+1)*x)
    plt.plot(x,psi_exact,label='Analytical')
    y = []
    for j in range(N):
        y.append(psi[j][i])
    plt.plot(x,y,'--',label='Numerical')
    plt.title(f'For n={i+1}, E={E[i]:.6}')
    plt.xlabel('x')
    plt.ylabel('ψ(x)')
    plt.legend()
    plt.grid()
plt.suptitle('Particle in a Box using Finite Difference Method')
plt.tight_layout()
plt.show()