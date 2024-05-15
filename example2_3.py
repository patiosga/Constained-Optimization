from sympy import Symbol
from main_solver import main_solver_two_constraints


# Ορίζω τις μεταβλητές
x1 = Symbol('x1', real=True)
x2 = Symbol('x2', real=True)
x3 = Symbol('x3', real=True)

# Ορίζω την συνάρτηση f(x)
main_func = 400*x1**2 + 800*x2**2 + 200*x1*x2 + 1600*x3**2 + 400*x2*x3

# Ορίζω τους περιορισμούς
g1 = x1 + x2 + 1.5*x3 - 1.2
g2 = x1 + x2 + x3 - 1

main_solver_two_constraints(main_func, [g1, g2], [x1, x2, x3])