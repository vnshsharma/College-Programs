import numpy as np 
import matplotlib.pyplot as plt 
def V(x,V0=10, L=1):
    potential = np.zeros_like(x)
    for i in range(len(x)):
        if -L/2 <= x[i] <=L/2:
            potential[i] = 0
        else:
            potential[i] = V0
    return potential
def euler(E,slope,x):
    h = x[1]-x[0]
    psi,phi = 0,slope
    psi_values = [psi]
    potential = V(x)
    for i in range(len(x)-1):
        psi += h*phi
        phi += h*(2*(potential[i]-E)*psi)
        psi_values.append(psi)
    return np.array(psi_values)
N=1000
L=1
x=np.linspace(-L,L,N+1)
En = 2.3
psi=euler(En,1,x)

plt.plot(x,psi,label='Wavefunction')
plt.plot(x,V(x)/10,'k--',label='Potential')
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()
plt.grid()
plt.show()