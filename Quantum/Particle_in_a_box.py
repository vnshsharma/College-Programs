import numpy as np
import matplotlib.pyplot as plt 
def euler(k,slope,N=1000):
    h=1/N
    psi,phi=0,slope
    psi_values = [psi]
    E = k**2/2
    for i in range(N):
        psi += h*phi
        phi += h*(-2*E*psi)
        psi_values.append(psi)
    return np.array(psi_values)
N = 1000
x = np.linspace(0,1,N+1)
plt.figure(figsize=(12,8))
plt.subplot(3,1,1)

# For n = 1
n = 1
k_true = n*np.pi
k_under = k_true*0.8
k_over = k_true*1.2
slope = np.sqrt(2)*n*np.pi
psi_exact = np.sqrt(2)*np.sin(n*np.pi*x)
plt.plot(x,euler(k_true,slope,N),label='Exact')
plt.plot(x,euler(k_under,slope,N),label='Overshoot')
plt.plot(x,euler(k_over,slope,N),label='Undershoot')
plt.plot(x,psi_exact,linestyle='--',label='Analytical')
plt.title('For n=1')
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()
plt.grid()

# For n=2
plt.subplot(3,1,2)
n = 2
k_true = n*np.pi
k_under = k_true*0.8
k_over = k_true*1.2
slope = np.sqrt(2)*n*np.pi
psi_exact = np.sqrt(2)*np.sin(n*np.pi*x)
plt.plot(x,euler(k_true,slope,N),label='Exact')
plt.plot(x,euler(k_under,slope,N),label='Undershoot')
plt.plot(x,euler(k_over,slope,N),label='Overshoot')
plt.plot(x,psi_exact,linestyle='--',label='Analytical')
plt.title('For n=2')
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()
plt.grid()

# For n=3
plt.subplot(3,1,3)
n = 3
k_true = n*np.pi
k_under = k_true*0.8
k_over = k_true*1.2
slope = np.sqrt(2)*n*np.pi
psi_exact = np.sqrt(2)*np.sin(n*np.pi*x)
plt.plot(x,euler(k_true,slope,N),label='Exact')
plt.plot(x,euler(k_under,slope,N),label='Overshoot')
plt.plot(x,euler(k_over,slope,N),label='Undershoot')
plt.plot(x,psi_exact,linestyle='--',label='Analytical')
plt.title('For n=3')
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()
plt.grid()

plt.suptitle('Particle in a Box')
plt.show()