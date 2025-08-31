import numpy as np
import matplotlib.pyplot as plt 
def euler(E,slope,N=1000):
    h=1/N
    psi,phi = 0,slope
    psi_values = [psi]
    for i in range(N):
        psi += h*phi
        phi += h*(-2*E*psi)
        psi_values.append(psi)
    return np.array(psi_values)
N = 1000
x = np.linspace(0,1,N+1)

plt.figure(figsize=(14,8))

plt.subplot(3,1,1)
# For n=1
n=1
slope = np.sqrt(2)*n*np.pi
E_true = ((n*np.pi)**2)/2
E_under = E_true*0.8
E_over = E_true*1.2
psi_exact = np.sqrt(2)*np.sin(n*np.pi*x)
plt.plot(x,euler(E_true,slope,N),label='Exact')
plt.plot(x,euler(E_under,slope,N),label='Undershoot')
plt.plot(x,euler(E_over,slope,N),label='Overshoot')
plt.plot(x,psi_exact,linestyle='--',label='Analytical')
plt.title('For n=1')
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()
plt.grid()

plt.subplot(3,1,2)
# For n=2
n=2
slope = np.sqrt(2)*n*np.pi
E_true = ((n*np.pi)**2)/2
E_under = E_true*0.8
E_over = E_true*1.2
psi_exact = np.sqrt(2)*np.sin(n*np.pi*x)
plt.plot(x,euler(E_true,slope,N),label='Exact')
plt.plot(x,euler(E_under,slope,N),label='Undershoot')
plt.plot(x,euler(E_over,slope,N),label='Overshoot')
plt.plot(x,psi_exact,linestyle='--',label='Analytical')
plt.title('For n=2')
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()
plt.grid()

plt.subplot(3,1,3)
# For n=3
n=3
slope = np.sqrt(2)*n*np.pi
E_true = ((n*np.pi)**2)/2
E_under = E_true*0.8
E_over = E_true*1.2
psi_exact = np.sqrt(2)*np.sin(n*np.pi*x)
plt.plot(x,euler(E_true,slope,N),label='Exact')
plt.plot(x,euler(E_under,slope,N),label='Undershoot')
plt.plot(x,euler(E_over,slope,N),label='Overshoot')
plt.plot(x,psi_exact,linestyle='--',label='Analytical')
plt.title('For n=3')
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()
plt.grid()

plt.suptitle("Particle in a Box")
plt.tight_layout()
plt.show()