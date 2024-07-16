import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

x = sym.symbols('x')

# Get the function from the user as a string
user_input = input("Enter the function to integrate (in terms of 'x'): ")

# Parse the user's input as a SymPy expression
user_function = sym.sympify(user_input)

# Perform the symbolic integration
integral_result = sym.integrate(user_function, x)

# Create a lambda function from the integral result
integral_function = sym.lambdify(x, integral_result, 'numpy')
#print(integral_function(x))

# Generate x values for the plot
x_values = np.linspace(-10, 10, 400)  # Adjust the range and number of points as needed

# Calculate corresponding y values for the integral result
y_values = [integral_function(x_val) for x_val in x_values]

# Plot the integral result
plt.plot(x_values, y_values, label=f'Integral of {user_function}')
plt.xlabel('x')
plt.ylabel('Integral')
plt.legend()
plt.grid()
plt.show()

