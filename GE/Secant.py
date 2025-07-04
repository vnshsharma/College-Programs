# Define the function

def f(x):
    return x**3 - 4*x - 9  # Example function

# Secant Method function
def secant(x0, x1, iterations):
    for i in range(iterations):
        if f(x1) - f(x0) == 0:
            print("Division by zero error.")
            return

        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        print(f"Iteration {i+1}: x2 = {x2}, f(x2) = {f(x2)}")

        x0 = x1
        x1 = x2

    print("Approximate root is:", x2)

# Example values
x0 = 2
x1 = 3
iterations = 10  # Number of iterations

# Call the function
secant(x0, x1, iterations)
