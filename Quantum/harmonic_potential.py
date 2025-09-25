import numpy as np 
import matplotlib.pyplot as plt 
def V(x):
    k=1
    return 0.5*k*x**2
def euler(E,slope,x):
    h = x[1]-x[0]
    psi,phi = 0,slope
    psi_values = [psi]
    potential = V(x)
    for i in range(len(x)-1):
        psi += h*phi
        phi += h*(2*(potential[i]-E)*psi)
        psi_values.append(psi)
    psi = np.array(psi_values)
    psi /= (np.sqrt(np.trapezoid(psi**2,x)))
    return psi
N = 2000
x = np.linspace(-5,5,N+1)
slope = 1
E_low = [0.5,1.5,2.5,12.5]
for E in E_low:
    n = 1
    psi = euler(E,slope,x)
    plt.plot(x,psi+E,label=f'E={E}')
plt.plot(x,V(x),'k--')
plt.legend()
plt.grid()
plt.show()