from sympy import symbols, lambdify
import numpy as np
from scipy.optimize import fsolve


if __name__ == '__main__':
    # Define symbols
    x, y = symbols('x y')

    # Non-linear system of equations (modified)
    equation1 = x**3 - y  # Circle equation with radius sqrt(2)
    equation2 = x - y  # Simpler non-linear equation

    # Convert equations to lambdify functions for numerical evaluation
    f1 = lambdify((x, y), equation1)
    f2 = lambdify((x, y), equation2)

    # Initial guess for the solution (adjust as needed)
    initial_guess = (0.9, -0.3)  # This is just a starting point

    # Use fsolve to find real solutions
    solutions = fsolve(lambda x: [f1(*x), f2(*x)], initial_guess)

    # solutions = fsolve([f1, f2], initial_guess)

    print("Real solutions:", solutions)
