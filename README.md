# 📚 Academic Numerical Methods & Physics Repository

This repository contains Python programs and study resources related to **Generic Elective (GE)** numerical methods and concepts from **Quantum Mechanics**.

---

## 📌 Sections

- [Generic Elective (GE)](#generic-elective-ge)
- [Quantum Mechanics](#quantum-mechanics)

---

## 📖 Generic Elective (GE)

This section includes implementations and formulas for essential numerical methods typically taught in **Generic Elective (GE)** courses.

---

### 🔹 Bisection Method

**Description:**  
A root-finding method that repeatedly halves an interval to locate a root of a given equation.

**Formula:**  

If a function \( f(x) \) changes sign over an interval \([a, b]\), then the root lies within that interval.  
At each step:
\[
c = \frac{a + b}{2}
\]
If \( f(c) \times f(a) < 0 \), then the root lies in \([a, c]\).  
Otherwise, it lies in \([c, b]\).

---

### 🔹 Trapezoidal Rule

**Description:**  
A numerical integration method that approximates the area under a curve as a sum of trapezoid areas.

**Formula:**  
For \( n \) intervals:
\[
I = \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]
\]
Where:
- \( h = \frac{b - a}{n} \)
- \( a \) and \( b \) are integration limits.

---

### 🔹 Secant Method

**Description:**  
An iterative technique to approximate the root of a function using a secant line between two approximations.

**Formula:**  
Given two initial guesses \( x_0 \) and \( x_1 \),
\[
x_{n+1} = x_n - \frac{f(x_n) (x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}
\]

---

### 🔹 Lagrange Interpolation

**Description:**  
A polynomial interpolation technique that estimates the value of a function based on known data points.

**Formula:**  
Given data points \( (x_0, y_0), (x_1, y_1), \dots, (x_n, y_n) \), the interpolating polynomial is:
\[
P(x) = \sum_{i=0}^{n} y_i \cdot L_i(x)
\]
Where:
\[
L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}
\]

---

## 📖 Quantum Mechanics

This section will include Python programs and explanations related to core topics in **Quantum Mechanics**, such as:



(📌 **Coming Soon...**)

---