from sympy import Symbol
from main_solver import main_solver_one_constraint

# Ορίζω τις μεταβλητές
x1 = Symbol('x1')
x2 = Symbol('x2')

# Ορίζω την συνάρτηση f(x) = x1^3 + x2^3
main_func = x1**3 + x2**3

# Ορίζω τον περιορισμό g(x) = x1**2 + x2**2 - 4 = 0
g = x1**2 + x2**2 - 4

main_solver_one_constraint(main_func, [g], [x1, x2])



