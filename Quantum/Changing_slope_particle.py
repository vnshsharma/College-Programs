import numpy as np 
import matplotlib.pyplot as plt 
def euler(E,slope,N=1000):
    h = 1/N
    psi,phi = 0,slope
    psi_values = [psi]
    for i in range(N):
        psi += h*phi
        phi += h*(-2*E*psi)
        psi_values.append(psi)
    return np.array(psi_values)
n,N = 1,1000
x = np.linspace(0,1,N+1)
psi_exact = np.sqrt(2)*np.sin(n*np.pi*x)
E_exact = ((n*np.pi)**2)/2
slope = [3.8995,4.4396,4.9999]
plt.plot(x,psi_exact,color='black',label=f'Analytical')
for i in slope:
    psi_numerical = euler(E_exact,i,N)
    plt.plot(x,psi_numerical,linestyle='--',label=f'Numerical, Slope={i}')
plt.title("Particle in a Box")
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()
plt.grid()
plt.show()