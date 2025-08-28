import numpy as np  
import matplotlib.pyplot as plt 
# Numerical Method 
def euler(E, slope, N=1000):
    h = 1/N
    psi, phi = 0, slope
    psi_values = [psi]
    for i in range(N):
        psi += h*phi
        phi += h*(-2*E*psi)
        psi_values.append(psi)
    return np.array(psi_values)  
# Analytical Method 
def psiActual(x):
    return np.sqrt(2) * np.sin(n*np.pi*x)
# Parameters
n, N = 1, 1000
En = ((n*np.pi)**2)/2
slope1 = 4.4396  # Guess slope
slope2 = 4.9999  # Guess slope  -> some alpha time of slope1
slope3 = 5.3456  # Guess slope  -> some beta time of slope2

x = np.linspace(0,1,N+1)

# Numerical 
psi_numerical1 = euler(En, slope1, N)
psi_numerical2 = euler(En, slope2, N)
psi_numerical3 = euler(En, slope3, N)

plt.plot(x, psiActual(x), label="Analytical")
plt.plot(x, psi_numerical1, linestyle='--',color='black')
plt.plot(x, psi_numerical2, linestyle='--')
plt.plot(x, psi_numerical3, linestyle='--')
plt.title("Analytical vs Numerical")
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()
plt.grid()

plt.title("Particle in a Box")
plt.show()