import numpy as np 
import matplotlib.pyplot as plt 

N = 400
k = 100
m = 940
hcut = 197.3
x = np.linspace(-4,4,N)
h = x[1]-x[0]
b_val = [0,10,30]

# Build Hamiltonian
def hamiltonian(b):
    V = 0.5*k*x**2+(1/3)*b*x**3
    H = np.zeros((N,N))
    coeff = (hcut**2)/(m*h**2)
    for i in range(N):
        H[i,i] = coeff+V[i]
        if i>0:
            H[i,i-1] = -0.5*coeff
        if i<N-1:
            H[i,i+1] = -0.5*coeff
    return H,V

plt.figure(figsize=(12,10))
for idx,b in enumerate(b_val):
    H,V = hamiltonian(b)
    E,psi = np.linalg.eigh(H)

    print(f"for b = {b}; Ground state energy E=", round(E[1],4))

    plt.subplot(3,2,2*idx+1)
    plt.plot(x,V,'r',label=f'Potential (b={b})')
    plt.xlabel('x')
    plt.ylabel('V(x)')
    plt.title(f'Potential for b={b}')
    plt.grid()
    plt.legend()

    plt.subplot(3,2,2*idx+2)
    P = psi[:,0]**2
    P /= np.trapezoid(P, x)
    P_shifted = P * 300
    plt.plot(x,P_shifted,label=f'|ψ₀|², E={round(E[1],4)}')
    plt.plot(x,V,'k--',label='Potential')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.title(f'Probability Densities (b={b})')
    plt.fill_between(x,min(V),P_shifted,color='blue',alpha=0.3)
    plt.legend()
    plt.grid()


plt.suptitle('Anharmonic Oscillator',fontsize=16)
plt.tight_layout()
plt.show()    