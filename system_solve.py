import sympy as sym


def system_solve(equations):
    # Define symbols
    # x, y = sym.symbols('x y')

    # # Define the variables
    # x, y = sym.symbols('x y')
    # variables = [x, y]

    # # Define the equations
    # eq1 = sym.Eq(x**3 - y, 0)
    # eq2 = sym.Eq(x - y, 0)
    # equations = [eq1, eq2]

    solution = sym.solve([eq for eq in equations])
    print("Solution:", solution)

