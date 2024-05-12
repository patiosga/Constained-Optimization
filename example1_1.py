from sympy import Symbol
from main_solver import main_solver_one_constraint

# Ορίζω τις μεταβλητές
x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')

# Ορίζω την συνάρτηση f(x) = x1^2 + x2^2 + x3^2
main_func = x1**2 + x2**2 + x3**2

# Ορίζω τον περιορισμό g(x) = x1 + x2 + x3 - 1 = 0
g = x1 + x2 + x3 - 1

main_solver_one_constraint(main_func, [g], [x1, x2, x3])



