# Function to integrate
def f(x):
    return x**2  # example: f(x) = x^2

# Trapezoidal Rule function
def trapezoidal(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        result += 2 * f(x)
    
    result *= (h / 2)
    return result

# Inputs
a = 0       # lower limit
b = 2       # upper limit
n = 4       # number of intervals

# Output
integral = trapezoidal(a, b, n)
print("Approximate value of integral:", integral)
