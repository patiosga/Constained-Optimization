from sympy import symbols, lambdify
import numpy as np
from scipy.optimize import fsolve


if __name__ == '__main__':
    # Define symbols
    x, y = symbols('x y')

    # Non-linear system of equations (modified)
    equation1 = x**2 - y  # Circle equation with radius sqrt(2)
    equation2 = x - y  # Simpler non-linear equation

 

    # Initial guess for the solution (adjust as needed)
    initial_guess = [0.9, -0.3]  # This is just a starting point

    # Use fsolve to find real solutions
    # solutions = fsolve(lambda x: [f1(*x), f2(*x)], initial_guess)
    # solutions = fsolve([equation1, equation2], initial_guess)

    # solutions = fsolve([f1, f2], initial_guess)

    # print("Real solutions:", solutions)


    import sympy as sym
    # Define the variables
    x, y = sym.symbols('x y')

    # Define the equations
    eq1 = sym.Eq(x**2 - y, 0)
    eq2 = sym.Eq(x - y, 0)
    eq3 = sym.Eq(x + y, 0)

    # Initial guess for the solution
    initial_guess = [-1, -1]

    # Use nsolve to find the solution
    solution = sym.solve([eq1, eq2, eq3], (x, y))
    print("Solution:", solution)

