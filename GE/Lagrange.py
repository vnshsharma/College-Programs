def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

x_points = [5, 6, 9, 11]
y_points = [12, 13, 14, 16]
x_to_find = 10

interpolated_value = lagrange_interpolation(x_points, y_points, x_to_find)
print(f"Interpolated value at x = {x_to_find} is {interpolated_value}") 