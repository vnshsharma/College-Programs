import numpy as np 
import matplotlib.pyplot as plt 
def V(x):
    V_outside = 1e3
    potential = np.zeros_like(x)
    for i in range(len(x)):
        if 0 <= x[i] <= 1:
            potential[i] = 0
        else:
            potential[i] = V_outside
    return potential
def euler(E, slope, x):
    N = 1000
    h = 1 / N
    psi, phi = 0, slope
    psi_values = [psi]
    potential = V(x)
    for i in range(N):
        psi += h * phi
        phi += h * (2 * (potential[i] - E) * psi)
        psi_values.append(psi)
    psi = np.array(psi_values)
    # normalize
    psi /= np.sqrt(np.trapezoid(psi**2, x))
    return psi
def exact(n, x):
    return np.sqrt(2) * np.sin(n * np.pi * x)
def E_exact(n):
    return (n*np.pi)**2/2
N = 1000
slope = 2
x = np.linspace(0, 1, N + 1)
En = [[4.4, 4.9, 5.4],[17.5, 19.5, 21.5],[39, 44, 49]]
plt.figure(figsize=(12,7))
for n in range(3):
    plt.subplot(3,1,n+1)
    for E in En[n]:
        psi = euler(E,slope,x)
        plt.plot(x,psi,label=f'Numerical, E={E}')
    plt.plot(x,exact(n+1,x),'k--',label=f'Analytical, E={round(E_exact(n+1),3)}')
    plt.title(f'For n={n+1}')
    plt.xlabel('x')
    plt.ylabel('ψ(x)')
    plt.grid()
    plt.legend()
plt.suptitle('Particle in a Box')
plt.tight_layout()
plt.show()