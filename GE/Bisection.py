# Define the function

def f(x):
    return x**3 - 4*x - 9  # Example function

# Bisection Method function
def bisection(a, b, iterations):
    if f(a) * f(b) >= 0:
        print("Bisection method not possible (f(a) and f(b) must have opposite signs).")
        return

    for i in range(iterations):
        c = (a + b) / 2
        print(f"Iteration {i+1}: Midpoint = {c}, f(c) = {f(c)}")

        if f(c) == 0.0:
            break

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    print("Approximate root is:", c)

# Example values
a = 2
b = 3
iterations = 10  # Number of iterations

# Call the function
bisection(a, b, iterations)
