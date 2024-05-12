from sympy import Symbol, diff, solve
import helper_funcs as hf
import numpy as np

if __name__ == "__main__":
    x = Symbol('x')
    y = Symbol('y')

    # def_expr = x**2 * y + y**2
    # print("Expression:", def_expr)

    # partial_dx = diff(def_expr, x)
    # partial_dy = diff(def_expr, y)

    # print("Partial derivative of f w.r.t. x:", partial_dx)
    # print("Partial derivative of f w.r.t. y:", partial_dy)
    # x_val = 2
    # y_val = 3
    # partial_dx_eval = partial_dx.subs({x: x_val, y: y_val})
    # partial_dy_eval = partial_dy.subs({x: x_val, y: y_val})
    # print("Partial derivative of f w.r.t. x at x=2, y=3:", partial_dx_eval)
    # print("Partial derivative of f w.r.t. y at x=2, y=3:", partial_dy_eval)


    # Working leading_principal_minor
    # matrix = [[1, 2], [2, 1]]
    # print("Matrix:", matrix)
    # print("Determinant of leading principal minor 1 :",  hf.leading_principal_minor(matrix, 1))
    # print("Determinant of leading principal minor 2 :", hf.leading_principal_minor(matrix, 2))


    # Testing hessian_matrix funcs
    # x = Symbol('x')
    # y = Symbol('y')
    # f = x**3 + y**3
    # vars = [x, y]
    # hessian = hf.calc_hessian_matrix(f, vars)
    # print("Hessian matrix:", hessian)
    # var_values = {y:3, x:2}
    # hessian_value = hf.hessian_matrix_value(hessian, var_values)
    # print("Hessian matrix value at x=2, y=3:", hessian_value)
    

    # Random testing
    f = x
    for i in range(5):
        f += x**i

    print(f)

