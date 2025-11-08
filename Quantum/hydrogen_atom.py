import numpy as np
import matplotlib.pyplot as plt 
N = 400
x = np.linspace(1e-7,4,N)
h = x[1]-x[0]
e = 3.795
hcut = 1973
m = 0.511e6
V = -(e**2)/x
coeff = (hcut**2)/(2*m*h**2)
H = np.zeros((N,N))
for i in range(N):
    H[i,i] = 2*coeff+V[i]
    if i>0:
        H[i,i-1] = -coeff
    if i<N-1:
        H[i,i+1] = -coeff
E,psi = np.linalg.eigh(H)
psi /= np.sqrt(np.trapezoid(psi**2,x))
for idx,n in enumerate([1,2]):
    plt.subplot(1,2,idx+1)
    plt.plot(x,psi[:,n]**2,label=f'Energy={E[n]:.2f}')
    plt.title(f'n={n}')
    plt.xlabel('x')
    plt.ylabel('Energy')
    plt.legend()
    plt.grid()
plt.suptitle('Hydrogen Atom Model')
plt.tight_layout()
plt.show() 