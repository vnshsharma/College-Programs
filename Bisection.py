# Define the function whose root we want to find
def f(x):
    return x**3 - 4*x - 9

# Bisection Method
def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method not possible (f(a) and f(b) must have opposite signs).")
        return None

    c = a
    while (b - a) >= tol:
        # Middle point
        c = (a + b) / 2

        # Check if middle point is root
        if f(c) == 0.0:
            break

        # Decide the side to repeat the steps
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c

# Example values
a = 2
b = 3
tolerance = 0.0001

# Call the method
root = bisection(a, b, tolerance)

# Print result
if root is not None:
    print("The root is:", root)
