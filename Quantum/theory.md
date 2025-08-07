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

## 🧑‍💻 Sample Code (Python)

```python
def f(x, y):
    return x + y  # Example: dy/dx = x + y

def euler(x0, y0, h, x_end):
    x = x0
    y = y0
    print(f"x = {x:.4f}, y = {y:.4f}")
    
    while x < x_end:
        y = y + h * f(x, y)
        x = x + h
        print(f"x = {x:.4f}, y = {y:.4f}")

# Initial conditions
x0 = 0
y0 = 1
h = 0.1
x_end = 1

euler(x0, y0, h, x_end)
