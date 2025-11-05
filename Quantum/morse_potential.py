import numpy as np 
import matplotlib.pyplot as plt 
m = 940e6
De  = 4.75
a = 1.94
hcut = 1973
re = 0.74
L = 2
N = 2000
r = np.linspace(re-L,re+L,N)
h = r[1]-r[0]
V_morse = De*(1-np.exp(-a*(r-re)))**2
k = 2*De*a**2
V_harmonic = 0.5*k*(r-re)**2
def Hamiltionian(V):
    H = np.zeros((N,N))
    coeff = (hcut**2)/(2*m*h**2)
    for i in range(N):
        H[i,i] = 2*coeff+V[i]
        if i>0:
            H[i,i-1] = -coeff
        if i<N-1:
            H[i,i+1] = -coeff
    E,psi = np.linalg.eigh(H)
    psi /= np.sqrt(np.trapezoid(psi**2,r))
    return E,psi
E_morse,psi_morse = Hamiltionian(V_morse)
E_harmonic,psi_harmonic = Hamiltionian(V_harmonic)
plt.figure(figsize=(10,6))
plt.plot(r,V_morse,color='black',label='Morse Potential')
plt.plot(r,V_harmonic,'--',label='Harmonic Potential')
plt.axhline(De,color='black',linestyle='--',label='Dissociation Energy')
states = [0,1,2,3,10,20]
for n in states:
    plt.plot(r,psi_morse[:,n]*0.05+E_morse[n],label=f'Morse n={n}, E={E_morse[n]:.2f}')
    plt.plot(r,psi_harmonic[:,n]*0.05+E_harmonic[n],label=f'Morse n={n}, E={E_harmonic[n]:.2f}',linestyle='--')
plt.title("Morse Potential")
plt.xlabel('r')
plt.ylabel('Energy')
plt.grid()
plt.legend(fontsize=7)
plt.ylim(0,9)
plt.show()
print("Energy levels:")
print(" n    E_morse        E_harm")
for n in states:
    print(f"{n:2d}   {E_morse[n]:10.4f}   {E_harmonic[n]:10.4f}")
reduced_mass = m/2
print(f'Reduced Mass: {reduced_mass:.2e}')