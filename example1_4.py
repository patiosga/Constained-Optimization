from sympy import Symbol
from main_solver import main_solver


# Ορίζω τις μεταβλητές
x1 = Symbol('x1')
x2 = Symbol('x2')

# Ορίζω την συνάρτηση f(x) = x1 + x2
main_func = x1 + x2

# Ορίζω τον περιορισμό g(x) = x1**2 + x2**2 - 2 = 0
g = x1**2 + x2**2 - 2

main_solver(main_func, [g], [x1, x2])