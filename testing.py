from sympy import Symbol, diff, solve
import helper_funcs as hf
import numpy as np


from sympy import Symbol, sympify

def my_function(x, y):
  z = x**2 + y**3  # Replace this with your actual function
  return sympify(z)  # Convert to symbolic expression (optional)


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
    

    import numpy as np

    x_min, x_max = -2, 2
    y_min, y_max = -2, 2
    resolution = 50

    x = np.linspace(x_min, x_max, resolution)
    y = np.linspace(y_min, y_max, resolution)
    X, Y = np.meshgrid(x, y)

    Z = np.zeros_like(X)
    X_flat = X.flatten()  # Reshape X to a 1D array
    Y_flat = Y.flatten()  # Reshape Y to a 1D array

    for i in range(resolution):
      for j in range(resolution):
        Z[i, j] = my_function(X_flat[i * resolution + j], Y_flat[i * resolution + j]).evalf()  # Evaluate the function

    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='viridis')  # Adjust 'cmap' for colormap

    # Optional: Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Function Visualization')

    # Example points
    highlight_x = [0, 1]
    highlight_y = [0, -1]
    highlight_z = [my_function(x, y) for x, y in zip(highlight_x, highlight_y)]

    ax.scatter(highlight_x, highlight_y, highlight_z, c='red', marker='o', s=80)


    plt.show()



