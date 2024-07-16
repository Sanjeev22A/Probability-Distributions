from sympy import sympify

# Convert a string to a SymPy expression
expression_str = "x**2 + 2*x + 1+2"
expression = sympify(expression_str)

# Now, 'expression' is a SymPy expression that represents the quadratic equation.

# You can perform symbolic operations on the expression
simplified_expression = expression.simplify()

# 'simplified_expression' is a simplified version of the original expression.
print(expression,simplified_expression,sep="\n")
