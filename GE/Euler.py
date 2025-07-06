import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

def exact_solution(x):
    return 2 * np.exp(x) - x - 1

x0 = 0
y0 = 1
h = 0.1
x_end = 2

x_values = np.arange(x0, x_end + h, h)
n = len(x_values)

y_values = np.zeros(n)
y_values[0] = y0

for i in range(1, n):
    y_values[i] = y_values[i-1] + h * f(x_values[i-1], y_values[i-1])

y_exact = exact_solution(x_values)

print("x\tEuler y\t\tExact y")
for i in range(n):
    print(f"{x_values[i]:.2f}\t{y_values[i]:.5f}\t{y_exact[i]:.5f}")

plt.plot(x_values, y_values, 'bo-', label="Euler's Method")
plt.plot(x_values, y_exact, 'r-', label="Exact Solution")
plt.title("dy/dx = x + y  |  Euler's Method vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
