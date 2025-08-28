import numpy as np 
import matplotlib.pyplot as plt 

# Numerical (Euler)
def solve(E, slope, N=1000):
    h = 1/N
    psi, phi = 0, slope
    k = E/2
    psi_values = [psi]
    for i in range(N):
        psi += h*phi
        phi += h*(-(k**2)*psi)   # corrected equation
        psi_values.append(psi)
    return np.array(psi_values)

# Analytical
def exact(x, n):
    return np.sqrt(2)*np.sin(n*np.pi*x)

# Parameters
N = 1000
x = np.linspace(0,1,N+1)

# Analytical curves for n=1,2,3
plt.plot(x, exact(x,n=1))

# Numerical for n=1
n = 1

E1 = 6
E2 = 6.25 
E3 = 7

slope = np.sqrt(2)*n*np.pi    # correct initial slope
psi_numerical1 = solve(E1, slope, N)
psi_numerical2 = solve(E2, slope, N)
psi_numerical3 = solve(E3, slope, N)

plt.plot(x, psi_numerical1, color='green', label="Numerical n=1")
plt.plot(x, psi_numerical2, '--', color='red', label="Numerical n=1")
plt.plot(x, psi_numerical3, color='black', label="Numerical n=1")

plt.legend()
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.title("Particle in a Box: Analytical vs Numerical (Euler)")
plt.grid()
plt.show() 