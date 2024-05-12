from sympy import Symbol, diff, solve
import numpy as np
import system_solve as sys_solve

def calc_partial_derivative(expr, var):
    return diff(expr, var)


def calc_gradient(func, vars):
    gradient = [calc_partial_derivative(func, var) for var in vars]
    return gradient


def calc_hessian_matrix(func, variables):
    '''
    Επιστρέφει έναν πίνακα vars x vars με συναρτήσεις (δεύτερες μερικες παράγωγοι)
    '''
    hessian_matrix = []
    for var in variables:
        hessian_matrix.append([calc_partial_derivative(calc_partial_derivative(func, var), second_var) for second_var in variables])
    return hessian_matrix


def hessian_matrix_value(hessian_matrix, var_values: dict):
    '''
    Υπολογισμός της τιμής του πίνακα H σε συγκεκριμένο σημείο x
    Η μεταβλητη var_values πρέπει να είναι λεξικο με τις τιμές των μεταβλητών --> π.χ. {x: 2, y: 3}
    '''
    for i, row in enumerate(hessian_matrix):
        for j, partial_derivative_func in enumerate(row):
            hessian_matrix[i][j] = partial_derivative_func.subs({var: value for var, value in var_values.items()})
    return hessian_matrix
    

   


def leading_principal_minor(matrix, i):
    '''
    Υπολογισμός πρωτεύουσας ελάσσονας ορίζουσας Δ_i
    '''
    matrix = np.array(matrix)  # Convert matrix to numpy array
    matrix = matrix[:i, :i]
    return np.linalg.det(matrix)



def is_positive_definite(matrix):
    pass


def is_negative_definite(matrix):
    pass


def find_critical_points(lagrange_func, equality_constraints):
    '''
    Εύρεση δεσμευμένων κρίσιμων σημείων της μέσω της συνάρτησης Lagrange
    '''
    pass