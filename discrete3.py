import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

def ReturnX(cof, yValue, x, y):
    xValue = cof * (yValue - y) + x
    return xValue

# Getting the inputs of range from the user
x_values = []
y_values = []

while True:
    temp = int(input("Enter x value:"))
    if temp == -1:
        break
    x_values.append(temp)

while True:
    temp = int(input("Enter y value:"))
    if temp == -1:
        break
    y_values.append(temp)

x_values = np.array(x_values)
y_values = np.array(y_values)
xy = x_values * y_values

# Calculating mean of x and y values
mean_x = np.mean(x_values)
mean_y = np.mean(y_values)
mean_xy = np.mean(xy)

# Calculating standard deviation of x and y values
sd_x = np.std(x_values)
sd_y = np.std(y_values)
standard_x = sd_x
standard_y = sd_y
expected_value = mean_xy

# Calculating correlation coefficient
covariance = expected_value - mean_x * mean_y
correlation_cof = covariance / (standard_x * standard_y)

# Displaying
print("Mean of x:", mean_x)
print("Standard Deviation of x:", standard_x)
print("Mean of y:", mean_y)
print("Standard Deviation of y:", standard_y)
print("E(XY):", mean_xy)
print("Covariance:",covariance)
print("Correlation Correlation coefficient:",correlation_cof)

# Plotting the scatter plot and correlation line
plt.scatter(y_values, x_values, color='blue', label='Data points')  # Note the swap of x and y here
line_y = np.linspace(min(y_values), max(y_values), 100)
line_x = (1 / correlation_cof) * (line_y - mean_y) + mean_x  # Rearranged formula
plt.plot(line_y, line_x, color='red', linestyle='dashed', label=f'Correlation Line for Predicting x from y (r={correlation_cof:.2f})')
plt.xlabel('y')
plt.ylabel('x')
plt.legend()
plt.grid()
plt.show()
