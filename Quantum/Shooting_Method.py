"""
The function `shooting_method` implements the shooting method to solve the Schrödinger equation for
a free particle in a box with a given energy.
"""
import math

def shooting_method():
    hcross = 1.0
    m = 1.0
    E = 5.0
    h = 0.01
    x_start = 0.0
    x_end = 1.0
    steps = int((x_end - x_start) / h)

    def V(x):
        return 0.0

    def integrate(slope):
        psi = 0.0
        phi = slope
        x = x_start
        for i in range(steps):
            k1_psi = h * phi
            k1_phi = h * (2*m/(hcross**2)) * (V(x) - E) * psi

            k2_psi = h * (phi + 0.5 * k1_phi)
            k2_phi = h * (2*m/(hcross**2)) * (V(x + 0.5*h) - E) * (psi + 0.5 * k1_psi)

            k3_psi = h * (phi + 0.5 * k2_phi)
            k3_phi = h * (2*m/(hcross**2)) * (V(x + 0.5*h) - E) * (psi + 0.5 * k2_psi)

            k4_psi = h * (phi + k3_phi)
            k4_phi = h * (2*m/(hcross**2)) * (V(x + h) - E) * (psi + k3_psi)

            psi += (k1_psi + 2*k2_psi + 2*k3_psi + k4_psi) / 6
            phi += (k1_phi + 2*k2_phi + 2*k3_phi + k4_phi) / 6
            x += h
        return psi

    slope_min = 0.0
    slope_max = 10.0

    for i in range(20):  # Fixed number of iterations
        slope_mid = (slope_min + slope_max) / 2
        if integrate(slope_min) * integrate(slope_mid) < 0:
            slope_max = slope_mid
        else:
            slope_min = slope_mid

    print("Best slope:", slope_mid)
    print("Final psi:", integrate(slope_mid))

shooting_method()
