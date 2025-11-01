import math
import numpy as np 
import matplotlib.pyplot as plt 
N = 400
k = 100
m = 940
hcut = 197.3
x = np.linspace(-4,4,N)
h = x[1]-x[0]
b_val = [0,10,30]
states = [0,1,2]
plot_idx = 1
omega = np.sqrt(k/m)
alpha = np.sqrt(m*omega/hcut)
def psi_ana(n,x,alpha):
    if n == 0:
        Hn = 1
    elif n == 1:
        Hn = 2*alpha*x
    elif n == 2:
        Hn = 4*(alpha*x)**2-2
    else:
        Hn = 0
    norm = np.sqrt(alpha/(np.sqrt(np.pi)*2**n*math.factorial(n)))
    return norm*Hn*np.exp(-0.5*(alpha*x)**2)
def ana_energy(n):
    return hcut*omega*(n+0.5)
ana_potential = 0.5*k*x**2
plt.figure(figsize=(14,10))
for b in b_val:
    potential = 0.5*k*x**2+(1/3)*b*x**3
    H = np.zeros((N,N))
    coeff = (hcut**2)/(2*m*h**2)
    for i in range(N):
        H[i,i] = 2*coeff+potential[i]
        if i>0:
            H[i,i-1] = -coeff
        if i<N-1:
            H[i,i+1] = -coeff
    E,psi = np.linalg.eigh(H)
    for n in states:
        # Numerical Prob. Density
        psi_num = psi[:,n]
        psi_norm = psi_num/np.sqrt(np.trapezoid(psi_num**2,x))
        psi_new = psi_norm*30+min(potential)
        # Analytical Prob. Density
        psi_analy = psi_ana(n,x,alpha)
        psi_ana_norm = psi_analy/np.sqrt(np.trapezoid(psi_analy**2,x))
        psi_ana_new = psi_ana_norm*30+min(potential)
        # Plot both Numerical and the Analytical Solution
        plt.subplot(3,3,plot_idx)
        plt.axhline(0,color='blue',linestyle=':')
        plt.plot(x,psi_new**2+E[n],color='blue',label=f'Energy Num. = {E[n]:.4}')
        plt.plot(x,psi_ana_new**2+ana_energy(n),color='green',label=f'Energy Ana. = {ana_energy(n):.4} ')
        plt.plot(x,potential,'r--',label='Anharmonic Potential')
        plt.plot(x,ana_potential,'g--',label='Harmonic Potential')
        plt.title(f'b={b}, n={n}')
        plt.xlabel('x')
        plt.ylabel("Energy")
        plt.ylim(0,1500)
        plt.grid()
        plt.legend()
        plot_idx += 1
plt.tight_layout()
plt.show()