import sympy as sym
import numpy as py
import matplotlib as plt

x=sym.symbols('x')
y=sym.symbols('y')

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
marginal_x = sym.integrate(user_function, (y))
marginal_x=marginal_x.subs({y:upper_y})-marginal_x.subs({y:lower_y})
print(upper_y)
# Calculate the marginal density of y, f(y)
marginal_y = sym.integrate(user_function, (x, lower_x, upper_x))



#display
print("Marginal Distribution of X (f(x)):", marginal_x)
print("Marginal Distribution of Y (f(y)):", marginal_y)
                        
