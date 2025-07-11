import numpy as np
import matplotlib.pyplot as plt

# Create theta values from 0 to pi
theta = np.linspace(0, np.pi, 200)

# Choose l and m
l = 1
m = 0

# Calculate Y(θ) based on l and m
if l == 0 and m == 0:
    Y = np.ones_like(theta)
elif l == 1 and m == 0:
    Y = np.cos(theta)
elif l == 2 and m == 0:
    Y = 0.5 * (3 * np.cos(theta)**2 - 1)
else:
    Y = np.zeros_like(theta)  # fallback for unsupported l,m

# Plotting the result
plt.plot(theta, Y)
plt.xlabel('Theta (radians)')
plt.ylabel('Y(θ)')
plt.title(f'Spherical Harmonic Y(θ) for l={l}, m={m}')
plt.grid(True)
plt.show()
