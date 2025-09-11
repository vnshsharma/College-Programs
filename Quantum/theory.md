# 📘 Euler's Method for Solving Ordinary Differential Equations

## 🧮 Overview

Euler’s Method is a **numerical technique** used to approximate solutions of **first-order ordinary differential equations (ODEs)** of the form:

\[
\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0
\]

It provides a way to compute the value of the function \( y \) at discrete points by taking small steps along the direction defined by the differential equation.

---

## 💡 Concept

The idea is to start at the initial condition and use the slope (given by the differential equation) to project the next value. This is done repeatedly to approximate the solution curve.

The update formula is:

\[
y_{n+1} = y_n + h \cdot f(x_n, y_n)
\]

Where:

- \( y_n \): current value of the solution
- \( x_n \): current value of the independent variable
- \( h \): step size
- \( f(x_n, y_n) \): the derivative at the current point

---

## 🧾 Algorithm

1. Set initial values \( x = x_0 \), \( y = y_0 \)
2. Choose a step size \( h \)
3. While \( x < x_{\text{end}} \):
   - Compute next \( x \) as:  
     \[
     x_{n+1} = x_n + h
     \]
   - Compute next \( y \) as:  
     \[
     y_{n+1} = y_n + h \cdot f(x_n, y_n)
     \]

---

## 🔢 Example

Solve the differential equation:

\[
\frac{dy}{dx} = x + y, \quad y(0) = 1
\]

Approximate the solution from \( x = 0 \) to \( x = 1 \) using a step size \( h = 0.1 \).

**Step-by-step (First 2 steps):**

1. \( x_0 = 0 \), \( y_0 = 1 \)
2. \( f(x_0, y_0) = 0 + 1 = 1 \)
3. \( y_1 = 1 + 0.1 \cdot 1 = 1.1 \)
4. \( f(x_1, y_1) = 0.1 + 1.1 = 1.2 \)
5. \( y_2 = 1.1 + 0.1 \cdot 1.2 = 1.22 \)

Continue this until \( x = 1 \)

---

## 📈 Accuracy

Euler’s method is a **first-order method**:
- Global error is \( \mathcal{O}(h) \)
- Local error per step is \( \mathcal{O}(h^2) \)

**Smaller step sizes** improve accuracy but require more computations.

---

## ⚠️ Limitations

- Not suitable for stiff equations
- Can be inaccurate if the function changes rapidly
- Errors accumulate over steps

---

# Finite Difference Method for Schrödinger’s Equation

## 🎯 Goal
We want to solve the **time-independent Schrödinger equation** in 1D:

\[
-\frac{\hbar^2}{2m} \frac{d^2 \psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)
\]

We set \(\hbar = 1\) and \(m = 1\) to simplify:

\[
-\frac{1}{2}\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)
\]

---

## 🟢 Step 1: Discretize the domain
- Domain: \(a \leq x \leq b\).  
- Divide into \(N\) equal grid points:

\[
x_0 = a, \; x_1, \; x_2, \dots, \; x_N = b
\]

- Grid spacing:

\[
h = \frac{b-a}{N}
\]

- Boundary conditions:  
  \(\psi(a) = \psi(b) = 0\) (Dirichlet).

We keep only **interior values**:

\[
\psi = \begin{bmatrix} \psi_1 \\ \psi_2 \\ \vdots \\ \psi_{N-1} \end{bmatrix}
\]

---

## 🟢 Step 2: Approximate the second derivative
Using central finite difference:

\[
\psi''(x_i) \approx \frac{\psi_{i-1} - 2\psi_i + \psi_{i+1}}{h^2}
\]

---

## 🟢 Step 3: Plug into Schrödinger equation
\[
-\frac{1}{2}\cdot \frac{\psi_{i-1} - 2\psi_i + \psi_{i+1}}{h^2} + V_i \psi_i = E\psi_i
\]

Expanding:

\[
-\frac{1}{2h^2} \psi_{i-1} + \left(\frac{1}{h^2} + V_i\right)\psi_i - \frac{1}{2h^2}\psi_{i+1} = E\psi_i
\]

---

## 🟢 Step 4: Matrix form
Collecting all equations gives a **matrix eigenvalue problem**:

\[
H \psi = E \psi
\]

The Hamiltonian \(H\) is **tridiagonal**:

- **Diagonal entries**:

\[
H_{ii} = \frac{1}{h^2} + V(x_i)
\]

- **Off-diagonal entries**:

\[
H_{i,i+1} = H_{i+1,i} = -\frac{1}{2h^2}
\]

---

## 🟢 Step 5: Example with 3 interior points
Suppose \(N = 4\) (so we have 3 interior points: \(\psi_1, \psi_2, \psi_3\)).  
The Hamiltonian becomes:

\[
H =
\begin{bmatrix}
\frac{1}{h^2}+V_1 & -\frac{1}{2h^2} & 0 \\
-\frac{1}{2h^2} & \frac{1}{h^2}+V_2 & -\frac{1}{2h^2} \\
0 & -\frac{1}{2h^2} & \frac{1}{h^2}+V_3
\end{bmatrix}
\]

The eigenvalue problem is:

\[
H
\begin{bmatrix}
\psi_1 \\ \psi_2 \\ \psi_3
\end{bmatrix}
= E
\begin{bmatrix}
\psi_1 \\ \psi_2 \\ \psi_3
\end{bmatrix}
\]

---

# Finite Difference Method — Infinite Square Well (Full worked example)

**Goal:** Solve the time-independent Schrödinger equation for an infinite square well using the finite difference method (FDM), and compare numerical results with the analytic solution.

---

## 1. Problem statement 

We solve the time-independent Schrödinger equation in 1D:

\[
-\tfrac{1}{2}\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)
\]

**Infinite square well** on \([0,L]\):

\[
V(x)=\begin{cases}
0,&0<x<L \\[6pt]
\infty,&\text{otherwise}
\end{cases}
\]

Boundary conditions (Dirichlet):

\[
\psi(0)=\psi(L)=0.
\]

Analytic (continuous) eigenvalues and eigenfunctions:

\[
E_n = \frac{\pi^2 n^2}{2 L^2},\qquad n=1,2,3,\dots
\]

\[
\psi_n(x) = \sqrt{\tfrac{2}{L}}\,\sin\!\Big(\frac{n\pi x}{L}\Big).
\]

For the worked example we set \( L=1 \), so

\[
E_n = \tfrac{\pi^2 n^2}{2}.
\]

---

## 2. Discretization (grid and notation)

Choose \( N \) interior grid points (exclude endpoints since \(\psi(0)=\psi(L)=0\)).

- Grid spacing:
\[
h = \frac{L}{N+1},
\]

- Grid points:
\[
x_i = i\,h,\qquad i=0,1,\dots,N+1,
\]

- Unknowns:
\[
\psi_1, \psi_2, \dots, \psi_N.
\]

---

## 3. Finite difference for the second derivative

At interior point \(x_i\):

\[
\psi''(x_i) \approx \frac{\psi_{i-1} - 2\psi_i + \psi_{i+1}}{h^2}.
\]

Insert into Schrödinger (with \(\hbar=m=1\) and \(V(x)=0\)):

\[
-\tfrac{1}{2}\cdot\frac{\psi_{i-1} - 2\psi_i + \psi_{i+1}}{h^2} = E\,\psi_i.
\]

Rearrange:

\[
-\frac{1}{2h^2}\psi_{i-1} + \frac{1}{h^2}\psi_i - \frac{1}{2h^2}\psi_{i+1} = E\psi_i.
\]

---

## 4. Matrix form — building the Hamiltonian

Collecting equations for all interior indices \(i=1,\dots,N\) yields:

\[
H\,\vec{\psi} = E\,\vec{\psi},\qquad \vec{\psi}=(\psi_1,\dots,\psi_N)^T.
\]

Hamiltonian matrix entries:

- Main diagonal:
\[
H_{ii} = \frac{1}{h^2} + V(x_i)
\]

- Off-diagonal (neighbors):
\[
H_{i,i+1} = H_{i+1,i} = -\frac{1}{2h^2}.
\]

Thus, for the infinite well:

\[
H = \frac{1}{h^2}\begin{pmatrix}
1 & -\tfrac{1}{2} & 0 & \cdots & 0 \\[6pt]
-\tfrac{1}{2} & 1 & -\tfrac{1}{2} & \cdots & 0 \\[6pt]
0 & -\tfrac{1}{2} & 1 & \ddots & 0 \\[6pt]
\vdots & & \ddots & \ddots & -\tfrac{1}{2} \\[6pt]
0 & \cdots & 0 & -\tfrac{1}{2} & 1
\end{pmatrix}.
\]

---

## 5. Small example (N=3)

Let \( L=1, N=3 \). Then \( h=1/4 \), so \( 1/h^2 = 16 \).

\[
H = \begin{pmatrix}
16 & -8 & 0 \\[6pt]
-8 & 16 & -8 \\[6pt]
0 & -8 & 16
\end{pmatrix}.
\]

Solve eigenvalue problem:

\[
H \vec{\psi} = E \vec{\psi}.
\]

This gives approximate energies:

- \(E_1 \approx 4.93\)  
- \(E_2 \approx 19.74\)  
- \(E_3 \approx 44.44\)

Compare with exact values for \(L=1\):

- \(E_1^{\text{exact}} = \pi^2/2 \approx 4.93\)  
- \(E_2^{\text{exact}} = 2\pi^2 \approx 19.74\)  
- \(E_3^{\text{exact}} = 9\pi^2/2 \approx 44.41\)

So the method works even for a small matrix.

---

## 6. Larger N numerical test (e.g. N=100)

- As \(N\) increases, approximation improves.  
- The first few eigenvalues match the analytic formula very accurately.  
- Eigenfunctions (discrete \(\psi_i\)) resemble sine waves.

---

## 7. Python code (example)

```python
import numpy as np
import matplotlib.pyplot as plt

L = 1.0
N = 100
h = L/(N+1)

# Build Hamiltonian
H = np.zeros((N,N))
for i in range(N):
    H[i,i] = 1/h**2
    if i > 0:
        H[i,i-1] = -1/(2*h**2)
    if i < N-1:
        H[i,i+1] = -1/(2*h**2)

# Solve eigenproblem
E, psi = np.linalg.eigh(H)

print("First 3 numerical energies:", E[:3])
print("Analytic:", [0.5*np.pi**2*n**2 for n in range(1,4)])

# Plot first eigenfunction
x = np.linspace(0,L,N+2)
psi_full = np.zeros(N+2)
psi_full[1:-1] = psi[:,0]
plt.plot(x, psi_full/np.max(np.abs(psi_full)), label="Numerical ψ1")
plt.plot(x, np.sqrt(2/L)*np.sin(np.pi*x/L), '--', label="Analytic ψ1")
plt.legend()
plt.show()
