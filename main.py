from sympy import Symbol, diff, solve

if __name__ == "__main__":
    x = Symbol('x')
    y = Symbol('y')

    def_expr = x**2 * y + y**2
    print("Expression:", def_expr)

    partial_dx = diff(def_expr, x)
    partial_dy = diff(def_expr, y)

    print("Partial derivative of f w.r.t. x:", partial_dx)
    print("Partial derivative of f w.r.t. y:", partial_dy)
    x_val = 2
    y_val = 3
    partial_dx_eval = partial_dx.subs({x: x_val, y: y_val})
    partial_dy_eval = partial_dy.subs({x: x_val, y: y_val})
    print("Partial derivative of f w.r.t. x at x=2, y=3:", partial_dx_eval)
    print("Partial derivative of f w.r.t. y at x=2, y=3:", partial_dy_eval)
