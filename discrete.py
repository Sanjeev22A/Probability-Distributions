import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import random
import math

def generate_random_variable(lower,upper):
    #no of data points
    num_points=random.randint(100,150)
    #num_points=100
    #selecting a random distribution
    distribution=random.choice(["exponential","binomial","poisson"])
    #distribution="binomial"
    if distribution == "exponential":
        lam=random.uniform(0.1,10.0)
        values=[random.expovariate(lam) for i in range(num_points)]
    elif distribution == "binomial":
        n = random.randint(1, 20)
        p = random.uniform(0.1, 0.9)
        values = [np.random.binomial(n, p) for _ in range(num_points)]
    elif distribution == "poisson":
        lmbda = random.uniform(1, 10)
        values = [np.random.poisson(lmbda) for _ in range(num_points)]
    else:
        raise ValueError("Unknown distribution")
    # Ensure values are within the specified range
    values = [value%upper+lower for value in values]

    return values
def ReturnX(cof,yValue,x,y,std_x,std_y):
    xValue=std_x*cof*(yValue-y)/std_y+x
    return xValue


x=sym.symbols('x')
y=sym.symbols('y')

#input from the user

user_input=input("Enter the joint probability density function(in terns of 'x' and 'y'):")

# Parsing user_input as a sympy expression
user_function = sym.sympify(user_input)

#Getting the inputs of range from the user

lower_x=float(input("Enter lower limit of x:"))
upper_x=float(input("Enter upper limit of x:"))
#lower_y=float(input("Enter lower limit of y:"))
#upper_y=float(input("Enter upper limit of y:"))

#generating x,y values
a=random.randint(1,10)
b=random.randint(1,10)
x_values=np.array(generate_random_variable(lower_x,upper_x))
y_values=a*x_values+b+np.random.normal(0,1,len(x_values))

#probability table
probability_array=[]
# Iterate through x and y values and calculate the probabilities
for i in range(len(x_values)):
    row = []
    for j in range(len(y_values)):
        probability = user_function.subs({x: x_values[i], y: y_values[j]})
        row.append(probability)
    probability_array.append(row)

probability_array=np.array(probability_array)
#normalizing the probability values

normalized_array = probability_array / np.sum(probability_array)


#axis 0 horizonal axis 1 vertical
# Calculate the marginal probability distributions for 'x' and 'y'
marginal_x = np.sum(normalized_array, axis=1)
marginal_y = np.sum(normalized_array, axis=0)

#calculating the mean and standard deviations of 'x'
mean_x=0

for x, marginal_prob in zip(x_values, marginal_x):
    mean_x += x * marginal_prob

mean_x=np.average(x_values,weights=marginal_x)
standard_x=(np.average((x_values-mean_x)**2,weights=marginal_x))**0.5

#calculating the mean and standard deviations of 'y'
mean_y=0
#mean_y=np.average(y_values,weights=marginal_y)
mean_y = 0
for y, marginal_prob_y in zip(y_values, marginal_y):
    mean_y += y * marginal_prob_y

standard_y=(np.average((y_values-mean_y)**2,weights=marginal_y))**0.5
#calculating E(xy)
expected_value=0
for i in range(len(x_values)):
    for j in range(len(y_values)):
        expected_value += x_values[i] * y_values[j] * normalized_array[i][j]
expected_value=float(expected_value)

#calculating covariance
covariance = expected_value-mean_x*mean_y
correlation_cof=covariance/(standard_x*standard_y)

#displaying
print("Mean of x:", mean_x)
print("Standard Deviation of x:", standard_x)
print("Mean of y:", mean_y)
print("Standard Deviation of y:", standard_y)
print("E(XY):", expected_value)
print("Covariance between x and y:", covariance)
print("Correlation Coefficient:", correlation_cof)
print("Marginal X:",marginal_x)
print("Marginal Y:",marginal_y)




# Update the scatter plot label
if correlation_cof == float('inf'):
    label = 'Correlation: +∞ (X on Y)'
elif correlation_cof == float('-inf'):
    label = 'Correlation: -∞ (X on Y)'
elif isinstance(correlation_cof, complex):
    label = 'Correlation: Complex (X on Y)'
else:
    label = 'Correlation: {:.3f} (X on Y)'.format(correlation_cof)

plt.scatter(x_values, y_values, alpha=0.3, c='blue', label=label)



#x on y
plot_y=y_values
plot_x=[ReturnX(correlation_cof,value_y,mean_x,mean_y,standard_x,standard_y) for value_y in y_values]
plot_x=np.array(plot_x)
plt.plot(plot_x,plot_y,color='green',linestyle="dashed",label='X on Y')
#y on x
plot_x=x_values
plot_y=[ReturnX(correlation_cof,value_x,mean_y,mean_x,standard_y,standard_x) for value_x in x_values]
plot_y=np.array(plot_y)
plt.plot(plot_x,plot_y,color="blue",linestyle="dashed",label='Y on X')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()



