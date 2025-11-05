import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm
def sph_harm_sq(l,m,theta,phi):
    return np.abs(sph_harm(m,l,phi,theta))**2
theta = np.linspace(0,np.pi,100)
phi = np.linspace(0,2*np.pi,100)
phi,theta = np.meshgrid(phi,theta)
l_m = [(1,0),(1,1),(2,0),(2,1),(2,2)]
fig = plt.figure(figsize=(10,6))
for idx, (l,m) in enumerate(l_m):
    r = sph_harm_sq(l,m,theta,phi)
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    ax = fig.add_subplot(2,3,idx+1,projection='3d')
    ax.plot_surface(x,y,z)
    ax.set_title(f'l={l}, m={m}')
plt.tight_layout()
plt.show()