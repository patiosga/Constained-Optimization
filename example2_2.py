from sympy import Symbol
from main_solver import main_solver_two_constraints


# Ορίζω τις μεταβλητές
x1 = Symbol('x1', real=True)
x2 = Symbol('x2', real=True)
x3 = Symbol('x3', real=True)

# Ορίζω την συνάρτηση f(x) = x1**2 + x2**2 + x3**2
main_func = x1**2 + x2**2 + x3**2

# Ορίζω τους περιορισμούς
# g1(x) = x1 + x2 + x3 - 1
# g2(x) = x2 - x1
g1 = x1 + x2 + x3 - 1
g2 = x2 - x1

main_solver_two_constraints(main_func, [g1, g2], [x1, x2, x3])