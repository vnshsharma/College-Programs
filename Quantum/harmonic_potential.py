import math 
import numpy as np 
import matplotlib.pyplot as plt 
N = 400 
x = np.linspace(-4,4,N)
m = 940 
hcut = 197.3
h = x[1]-x[0]
k = 100
omega = np.sqrt(k/m)
alpha = np.sqrt(m*omega/hcut)
def analytic(n,x,alpha):
    if n == 0:
        Hn = 1
    elif n == 1:
        Hn = 2*alpha*x
    elif n == 2:
        Hn = 4*(alpha*x)**2-2
    else:
        Hn = 0
    norm = np.sqrt(alpha/(np.sqrt(np.pi)*(2**n)*math.factorial(n)))
    return norm*Hn*np.exp(-0.5*(alpha*x)**2)
def analytic_energy(n):
    return (n+0.5)*hcut*omega
coeff = (hcut**2)/(2*m*h**2)
H = np.zeros((N,N))
V = 0.5*k*x**2
for i in range(N):
    H[i,i] = 2*coeff+V[i]
    if i>0:
        H[i,i-1] = -coeff
    if i<N-1:
        H[i,i+1] = -coeff
E,psi = np.linalg.eigh(H)
for i in range(N):
    psi[:,i] /= np.sqrt(np.trapezoid(psi[:,i]**2,x))
plt.plot(x,V,label='Potential')
print('n      Num. Energy     Ana. Energy')
for n in ([0,1,2]):
    plt.plot(x,psi[:,n]**2*80+E[n],label=f'n={n} Numerical')
    plt.plot(x,analytic(n,x,alpha)**2*80+analytic_energy(n),label=f'n={n} Analytical',linestyle='--',color='black')
    print(f'{n}      {E[n]:.2f}          {analytic_energy(n):.2f}')
plt.title("Harmonic Oscillator")
plt.xlabel('x')
plt.ylabel('Energy')
plt.legend()
plt.grid()
plt.show() 