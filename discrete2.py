import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import random

def generate_random_variable(lower, upper):
    num_points = 100
    distribution = random.choice(["exponential", "binomial", "poisson"])
    distribution = "binomial"
    
    if distribution == "exponential":
        lam = random.uniform(0.1, 10.0)
        values = [random.expovariate(lam) for i in range(num_points)]
    elif distribution == "binomial":
        n = random.randint(1, 20)
        p = random.uniform(0.1, 0.9)
        values = [np.random.binomial(n, p) for _ in range(num_points)]
    elif distribution == "poisson":
        lmbda = random.uniform(1, 10)
        values = [np.random.poisson(lmbda) for _ in range(num_points)]
    else:
        raise ValueError("Unknown distribution")
    
    values = [value % upper + lower for value in values]

    return values

def ReturnX(cof, yValue, x, y):
    xValue = cof * (yValue - y) + x
    return xValue

x = sym.symbols('x')
y = sym.symbols('y')

# Input from the user
user_input = input("Enter the joint probability density function (in terms of 'x' and 'y'): ")

# Parsing user_input as a sympy expression
user_function = sym.sympify(user_input)

# Getting the inputs of range from the user
lower_x = float(input("Enter lower limit of x: "))
upper_x = float(input("Enter upper limit of x: "))

# Generate x, y values
a = random.randint(1, 10)
b = random.randint(1, 10)
x_values = np.array(generate_random_variable(lower_x, upper_x))
y_values = a * x_values + b + np.random.normal(0, 1, len(x_values))

# Probability table
probability_array = []

# Iterate through x and y values and calculate the probabilities
for i in range(len(x_values)):
    row = []
    for j in range(len(y_values)):
        probability = user_function.subs({x: x_values[i], y: y_values[j]})
        row.append(probability)
    probability_array.append(row)

probability_array = np.array(probability_array)

# Normalizing the probability values
normalized_array = probability_array / np.sum(probability_array)

# Calculate the marginal probability distributions for 'x' and 'y'
marginal_x = np.sum(normalized_array, axis=1)
marginal_y = np.sum(normalized_array, axis=0)

# Calculate the mean and standard deviations of 'x'
mean_x = np.average(x_values, weights=marginal_x)
standard_x = (np.average((x_values - mean_x)**2, weights=marginal_x))**0.5

# Calculate the mean and standard deviations of 'y'
mean_y = np.average(y_values, weights=marginal_y)
standard_y = (np.average((y_values - mean_y)**2, weights=marginal_y))**0.5

# Calculate E(xy)
expected_value = np.sum(x_values[:, np.newaxis] * y_values * normalized_array)

# Calculate covariance
covariance = expected_value - mean_x * mean_y
correlation_cof = covariance / (standard_x * standard_y)

# Displaying
print("Mean of x:", mean_x)
print("Standard Deviation of x:", standard_x)
print("Mean of y:", mean_y)
print("Standard Deviation of y:", standard_y)
print("E(XY):", expected_value)
print("Covariance between x and y:", covariance)
print("Correlation Coefficient:", correlation_cof)
print("Marginal X:", marginal_x)
print("Marginal Y:", marginal_y)
print("X_values:", x_values)
print("Y_Values:", y_values)
print("The normalized probability array:", normalized_array)

# Initial correlation coefficient value
initial_value = 0.0

# Set up the figure and axis for the plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

# Set up the slider
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
slider = Slider(ax_slider, 'Correlation', -1.0, 1.0, valinit=initial_value)

# Scatter plot initialization
scatter_plot = plt.scatter(x_values, y_values, alpha=0.3, c='blue', label='Correlation: {:.3f} (X on Y)'.format(initial_value))

# Function to update the plot based on the slider value
def update(val):
    correlation_cof = slider.val

    # Update the scatter plot label
    label = 'Correlation: {:.3f} (X on Y)'.format(correlation_cof)
    scatter_plot.set_label(label)

    # Plotting lines for X on Y and Y on X
    plot_y = y_values
    plot_x = [ReturnX(correlation_cof, value_y, mean_x, mean_y) for value_y in y_values]
    plot_x = np.array(plot_x)
    plt.plot(plot_x, plot_y, color='green', linestyle="dashed", label='X on Y')

    plot_x = x_values
    plot_y = [ReturnX(correlation_cof, value_x, mean_y, mean_x) for value_x in x_values]
    plot_y = np.array(plot_y)
    plt.plot(plot_x, plot_y, color="blue", linestyle="dashed", label='Y on X')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()
    fig.canvas.draw_idle()

# Attach the update function to the slider
slider.on_changed(update)

# Display the initial plot
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
