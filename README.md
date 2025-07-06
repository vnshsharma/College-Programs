# 📚 Academic Numerical Methods & Physics Repository

This repository contains Python programs and study resources related to **Generic Elective (GE)** numerical methods and concepts from **Quantum Mechanics**. It is designed to help students understand numerical algorithms and computational techniques essential in scientific problem-solving, especially when analytical solutions are challenging or impossible.

---

## 📌 Sections

- [Generic Elective (GE)](#generic-elective-ge)
- [Quantum Mechanics](#quantum-mechanics)

---

## 📖 Generic Elective (GE)

This section includes Python implementations and mathematical formulas for essential numerical methods typically taught in **Generic Elective (GE)** courses. These methods help find approximate solutions to problems involving equations, integrals, and interpolation. Each program includes clear logic, formulas, and explanation of practical applications.

---

### 🔹 Bisection Method

**Description:**  
A simple and reliable root-finding method based on the principle of the **Intermediate Value Theorem**. It requires an interval `[a, b]` where the function changes sign, i.e., `f(a) * f(b) < 0`. The method repeatedly bisects the interval and selects the subinterval in which the function changes sign until the root is located within a desired level of accuracy.

**How it works:**  
- Choose an initial interval `[a, b]`
- Check the sign of `f(a) * f(b)`
- Bisect the interval and select the half where the sign change occurs
- Repeat until the interval is sufficiently small

**Advantages:**  
✅ Guaranteed convergence if the function is continuous and the initial interval has a root  
✅ Simple to understand and implement  

**Where to use:**  
Ideal for finding roots of continuous functions when the root lies within a known interval and the function changes sign.

---

### 🔹 Trapezoidal Rule

**Description:**  
A numerical integration technique that approximates the area under a curve by dividing the total area into small trapezoids rather than rectangles. It then computes the total area by summing up the areas of these trapezoids.

**How it works:**  
- Divide the total interval `[a, b]` into `n` subintervals
- Calculate the function values at each point
- Apply the trapezoidal rule formula to approximate the integral

**Advantages:**  
✅ More accurate than simple rectangular methods  
✅ Easy to implement for both evenly and unevenly spaced data  

**Where to use:**  
Useful for estimating definite integrals when:
- Analytical integration is complicated
- Working with tabulated experimental data  
- Evaluating definite integrals in physics and engineering problems  

---

### 🔹 Secant Method

**Description:**  
An iterative numerical technique for finding the root of a function using secant lines through successive approximations. Unlike the Newton-Raphson method, it does not require the derivative of the function, making it useful when the derivative is difficult or unknown.

**How it works:**  
- Start with two initial guesses, `x0` and `x1`
- Compute a new approximation using the secant formula  
- Repeat the process until convergence

**Advantages:**  
✅ Faster than the Bisection Method  
✅ Does not need derivative calculations  
✅ Suitable for non-differentiable or complex functions  

**Where to use:**  
Ideal when:
- Derivatives are difficult or impractical to compute  
- Quick convergence is preferred with reasonable initial guesses  

---

### 🔹 Lagrange Interpolation

**Description:**  
A polynomial interpolation technique used to estimate unknown values of a function using a given set of known data points. It constructs a polynomial passing through all given points and evaluates the function at desired positions.

**How it works:**  
- Given `n` data points `(x0, y0), (x1, y1), ... (xn, yn)`  
- Construct the Lagrange polynomial using the formula:
  \[
  P(x) = \sum_{i=0}^{n} y_i \cdot L_i(x)
  \]
  where \( L_i(x) \) are the Lagrange basis polynomials

**Advantages:**  
✅ Simple to understand and apply for small data sets  
✅ Provides exact interpolation at given points  

**Where to use:**  
- Estimating unknown values between known data points  
- Numerical solutions in physics, engineering, and data analysis  
- Approximating complex functional relationships  

---

## 📖 Quantum Mechanics

This section will feature Python programs and explanations related to fundamental topics in **Quantum Mechanics**, aiming to make theoretical concepts computationally approachable and visually understandable. It will include numerical simulations and solutions to famous quantum models.

---
