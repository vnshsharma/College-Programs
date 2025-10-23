import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm_y

# Function to compute probability density using sph_harm_y
def sph_harm_y_abs2(n, m, theta, phi):
    Ynm = sph_harm_y(n, m, theta, phi)  # Compute spherical harmonic
    r = np.abs(Ynm)**2                   # Probability density |Y|^2
    return r

# θ = polar angle, φ = azimuthal angle
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

# List of (l, m) values to plot
lm_list = [(1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]

# Create figure
fig = plt.figure(figsize=(10, 6))

for i, (l, m) in enumerate(lm_list):
    r = sph_harm_y_abs2(l, m, theta, phi)  
    
    # Convert spherical to Cartesian
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    # Create subplot
    ax = fig.add_subplot(2, 3, i+1, projection='3d')
    ax.plot_surface(x, y, z,)

plt.tight_layout()
plt.show()