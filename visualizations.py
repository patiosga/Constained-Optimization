from sympy import Symbol, diff, solve
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify


def my_function_1_f(x, y):
  z = x + y 
  return sympify(z)  # Convert to symbolic expression (optional)

def my_function_1_g(x, y):
  z = x**2 + y**2 - 2 
  return sympify(z) 

def my_function_2_f(x, y):
  z = x**3 + y**3 
  return sympify(z) 

def my_function_2_g(x, y):
  z = x**2 + y**2 - 4 
  return sympify(z) 


def visualize_example1_0():
    x = Symbol('x')
    y = Symbol('y')


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
        Z[i, j] = my_function_1_f(X_flat[i * resolution + j], Y_flat[i * resolution + j]).evalf()  # Evaluate the function


    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='viridis')  # Adjust 'cmap' for colormap

    # Optional: Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_title('f = x + y, g = x^2 + y^2 - 2 = 0')

    # Example points
    x = np.array([-1, 1])
    y = np.array([-1, 1])
    z = my_function_1_f(x, y)
    print(z)
    ax.scatter(x, y, z, color='red', alpha=1)


    # Plotting the constraint g = 0 as a circle
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = np.sqrt(2) * np.cos(theta)
    y_circle = np.sqrt(2) * np.sin(theta)
    z_circle = (-4) * np.ones(100)

    ax.plot(x_circle, y_circle, z_circle, color='blue', label='g = 0')
    ax.legend()


    ax.plot([-1, -1], [-1, -1], [-4, -2], color='black', linestyle='--')
    ax.plot([1,1], [1,1], [-4, 2], color='black', linestyle='--')

    plt.show()



def visualize_example1_2():
    x = Symbol('x')
    y = Symbol('y')


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
        Z[i, j] = my_function_2_f(X_flat[i * resolution + j], Y_flat[i * resolution + j]).evalf()  # Evaluate the function


    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='viridis')  # Adjust 'cmap' for colormap

    # Optional: Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_title('f = x^3 + y^3, g = x^2 + y^2 - 4 = 0')

    # Example points
    x = np.array([-2, 0, 2, 0, -np.sqrt(2), np.sqrt(2)])
    y = np.array([0, 2, 0, -2, -np.sqrt(2), np.sqrt(2)])
    z = my_function_2_f(x, y)
    ax.scatter(x, y, z, color='red', alpha=1)


    # Plotting the constraint g = 0 as a circle
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = 2 * np.cos(theta)
    y_circle = 2 * np.sin(theta)
    z_circle = (-15) * np.ones(100)

    ax.plot(x_circle, y_circle, z_circle, color='blue', label='g = 0')
    ax.legend()

    for i in range(len(x)):
      ax.plot([x[i], x[i]], [y[i], y[i]], [-15, z[i]], color='black', linestyle='--')

    plt.show()




if __name__ == '__main__':
    visualize_example1_0()
    visualize_example1_2()