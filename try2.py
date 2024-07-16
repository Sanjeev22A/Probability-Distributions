import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

def generate_x(y_val, expected_x, expected_y, standard_x, standard_y, correlation_cof):
    x_val = (standard_x * correlation_cof / standard_y * (y_val - expected_y)) + expected_x
    return x_val

# Define symbolic variables
x = sym.symbols('x')
y = sym.symbols('y')

# Input from the user
user_input = input("Enter the joint probability density function (in terms of 'x' and 'y'): ")

# Getting the limits
lower_x = float(input("Enter lower limit of x: "))
upper_x = float(input("Enter upper limit of x: "))
lower_y = float(input("Enter lower limit of y: "))
upper_y = float(input("Enter upper limit of y: "))

# Parsing user_input as a sympy expression
user_function = sym.sympify(user_input)

# Calculate the marginal density of x, f(x)
marginal_x = sym.integrate(user_function, (y, lower_y, upper_y))

# Calculate the marginal density of y, f(y)
marginal_y = sym.integrate(user_function, (x, lower_x, upper_x))

# Calculate E(XY)
expected_xy = sym.integrate(x * y * user_function, (x, lower_x, upper_x), (y, lower_y, upper_y))

# Calculate E(X)
expected_x = sym.integrate(x * marginal_x, (x, lower_x, upper_x))

# Calculate E(Y)
expected_y = sym.integrate(y * marginal_y, (y, lower_y, upper_y))

# Covariance
covariance = expected_xy - expected_x * expected_y

# Variance and Standard Deviation of X and Y
variance_x = sym.integrate((x - expected_x)**2 * marginal_x, (x, lower_x, upper_x))
standard_deviation_x = sym.sqrt(variance_x)
variance_y = sym.integrate((y - expected_y)**2 * marginal_y, (y, lower_y, upper_y))
standard_deviation_y = sym.sqrt(variance_y)

# Correlation Coefficient
correlation_coefficient = covariance / (standard_deviation_x * standard_deviation_y)

# Regression line X on Y
y_values = np.linspace(lower_y, upper_y, 1000)
x_values = [generate_x(y_val, expected_x, expected_y, standard_deviation_x, standard_deviation_y, correlation_coefficient).evalf() for y_val in y_values]

# Plotting X on Y
plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(x_values, y_values, label='Correlation Graph (X on Y)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Regression line Y on X
x_values = np.linspace(lower_x, upper_x, 1000)
y_values = [generate_x(x_val, expected_y, expected_x, standard_deviation_y, standard_deviation_x, correlation_coefficient).evalf() for x_val in x_values]

# Plotting Y on X
plt.subplot(122)
plt.plot(x_values, y_values, label='Correlation Graph (Y on X)')
plt.xlabel('Y')
plt.ylabel('X')
plt.legend()

plt.tight_layout()
plt.show()


# Print the results
print("Marginal Distribution of X (f(x)):", marginal_x)
print("Marginal Distribution of Y (f(y)):", marginal_y)
print("E(XY):", expected_xy)
print("E(X):", expected_x)
print("E(Y):", expected_y)
print("Covariance:", covariance)
print("Standard Deviation of X:", standard_deviation_x)
print("Standard Deviation of Y:", standard_deviation_y)
print("The Correlation Coefficient:", correlation_coefficient)
