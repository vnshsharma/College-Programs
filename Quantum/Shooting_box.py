import math
import matplotlib.pyplot as plt

# RK4 solver for Schrödinger equation
def solve(E, N=1000):
    h = 1 / N
    xVals = [i * h for i in range(N+1)]  # grid from 0 to 1
    psi, phi = 0.0, 1.0   # initial conditions
    values = [psi]
    
    for step in range(N):
        k1psi = h * phi
        k1phi = h * (-2 * E * psi)

        k2psi = h * (phi + k1phi/2)
        k2phi = h * (-2 * E * (psi + k1psi/2))

        k3psi = h * (phi + k2phi/2)
        k3phi = h * (-2 * E * (psi + k2psi/2))

        k4psi = h * (phi + k3phi)
        k4phi = h * (-2 * E * (psi + k3psi))

        psi = psi + (k1psi + 2*k2psi + 2*k3psi + k4psi) / 6
        phi = phi + (k1phi + 2*k2phi + 2*k3phi + k4phi) / 6

        values.append(psi)
    
    # --- Normalization (Trapezoidal Rule) ---
    norm = 0.0
    for i in range(N):
        norm += (values[i]**2 + values[i+1]**2) * h / 2
    norm = math.sqrt(norm)

    for i in range(len(values)):
        values[i] = values[i] / norm
    # ----------------------------------------

    return xVals, values, psi

# Analytical solution for n=1
def psiAnalytical(xVals):
    return [math.sqrt(2) * math.sin(math.pi * xi) for xi in xVals]

# Find correct energy via bisection
Eleft, Eright = 4.0, 6.0
for iteration in range(50):
    Emid = (Eleft + Eright) / 2
    xVals, values, psiLast = solve(Emid)
    if abs(psiLast) < 1e-6:   # tolerance check
        break
    if psiLast > 0:
        Eleft = Emid
    else:
        Eright = Emid

# Solutions
xVals, psiUnder, psiLast = solve(4.0)
xVals, psiCorrect, psiLast = solve(Emid)
xVals, psiOver, psiLast = solve(6.0)
psiExact = psiAnalytical(xVals)

# Plot
plt.plot(xVals, psiUnder, label="E=4.0 (under)")
plt.plot(xVals, psiCorrect, label=f"E={Emid:.4f} (correct)")
plt.plot(xVals, psiOver, label="E=6.0 (over)")
plt.plot(xVals, psiExact, "k--", label="Analytical")
plt.title("Wavefunction for n=1: Numerical vs Analytical")
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.legend()
plt.grid()
plt.show() 