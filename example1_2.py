from sympy import Symbol
from main_solver import main_solver


# Ορίζω τις μεταβλητές
x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')

# Ορίζω την συνάρτηση f(x) = x1*x2*x3
main_func = x1*x2*x3

# Ορίζω τον περιορισμό g(x) = x1*x2 + x1*x3 + x2*x3 - 6 = 0
g = x1*x2 + x1*x3 + x2*x3 - 6

main_solver(main_func, [g], [x1, x2, x3])