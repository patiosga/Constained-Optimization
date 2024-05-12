import sympy as sym


def system_solve(functions):
    # Define symbols
    # x, y = sym.symbols('x y')

    # # Define the equations
    # eq1 = sym.Eq(x**3 - y, 0)
    # eq2 = sym.Eq(x - y, 0)
    # equations = [eq1, eq2]
    equations = [sym.Eq(func, 0) for func in functions]

    solutions = sym.solve([eq for eq in equations])
        
    return solutions

