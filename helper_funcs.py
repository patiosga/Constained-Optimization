from sympy import diff, solve
import numpy as np
import system_solve as sys_solve
from copy import deepcopy

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


def hessian_matrix_value(hessian_matrix, point: dict):
    '''
    Υπολογισμός της τιμής του πίνακα H σε συγκεκριμένο σημείο x
    Η μεταβλητη var_values πρέπει να είναι λεξικο με τις τιμές των μεταβλητών --> π.χ. {x: 2, y: 3}
    '''
    resulting_matrix = [[0 for _ in hessian_matrix] for _ in hessian_matrix]
    
    for i, row in enumerate(hessian_matrix):
        for j, partial_derivative_func in enumerate(row):
            if (type(partial_derivative_func) == int) or (type(partial_derivative_func) == float):
                resulting_matrix[i][j] = partial_derivative_func  # αν είναι ήδη αριθμός δεν χρειάζεται να υπολογιστεί γιατί πετάει σφάλμα η subs
            else:
                resulting_matrix[i][j] = float(partial_derivative_func.subs({var: value for var, value in point.items()}))  # αντικατάσταση των τιμών των μεταβλητών στην συνάρτηση         
                
    return resulting_matrix
    

def leading_principal_minor(matrix, i):
    '''
    Υπολογισμός πρωτεύουσας ελάσσονας ορίζουσας Δ_i
    '''
    matrix = np.array(matrix)  # Convert matrix to numpy array
    matrix = matrix[:i, :i]
    return np.linalg.det(matrix)


def find_critical_points(lagrange_func_obj):
    '''
    Εύρεση δεσμευμένων κρίσιμων σημείων της μέσω της συνάρτησης Lagrange
    '''
    # Υπολογισμός των σημείων που λύνουν το σύστημα
    solution = sys_solve.system_solve(lagrange_func_obj.lagrangian_gradient)
    # Επιστρέφει λίστα λεξικών από τα σημεία που λυνουν το σύστημα: αναδελτα της συνάρτησης Lagrange = 0
    # π.χ. [{x: 2, y: 3, lambda: 1}, {x: 3, y: 4, lambda: 2}] -- Αν έχει μια μόνο λύση τότε επιστρέφει μόνο ενα λεξικό εκτός λίστας
    return solution


def sufficient_condition_second_grade_one_constraint(lagrange_func_obj, critical_points):
    '''
    Ικανή συνθήκη δεύτερης τάξης για την εύρεση του είδους των ακροτάτων
    '''
    points_classification = []  # Λίστα με τα σημεία και το είδος του ακρότατου σε μορφή tuple

    # Αν τα δεσμευμένα κρίσιμα σημεία είναι μόνο ένα τότε το μετατρέπω σε λίστα
    if type(critical_points) == dict:
        critical_points = [critical_points]

    # Υπολογισμός των Εσσιανών πινάκων της συνάρτησης Lagrange στα δεσμευμένα κρίσιμα σημεία
    hessian_values = [hessian_matrix_value(lagrange_func_obj.lagrangian_hessian, point) for point in critical_points]

    for i, hessian in enumerate(hessian_values):
        # Υπολογισμός των πρωτεύουσων ελάσσονων οριζουσών Δ_i για i = 3, 4, ..., n + 1 
        principal_minor_values = [leading_principal_minor(hessian, i) for i in range(3, len(lagrange_func_obj.variables) + 1)]
        
        # Έλεγχος αν οι πρωτεύουσες ελάσσονες ορίζουσες είναι όλες θετικές
        if all([minor < 0 for minor in principal_minor_values]):
            points_classification.append((critical_points[i], 'local minimum'))  # Το σημείο είναι τοπικό ελάχιστο
        # Έλεγχος αν οι πρωτεύουσες ελάσσονες ορίζουσες έχουν εναλλασσόμενο πρόσημο
        elif alternating_sign(principal_minor_values):
            points_classification.append((critical_points[i], 'local maximum'))  # Το σημείο είναι τοπικό μέγιστο
        else:
            points_classification.append((critical_points[i], 'not a local optimizer'))  # Το σημείο δεν μπορεί να κριθεί με την ικανή συνθήκη δεύτερης τάξης
    return points_classification


def alternating_sign(lista):
    '''
    Επιστρέφει True αν τα στοιχεία της λίστας έχουν εναλλασόμενο πρόσημο με το πρώτο να είναι θετικό (Εδώ η Δ_3)
    '''
    if lista[0] > 0:
        return all(lista[i] * lista[i + 1] < 0 for i in range(len(lista) - 1))
    return False


def sufficient_condition_second_grade_two_constraints(lagrange_func_obj, critical_points):
    '''
    Ικανή συνθήκη δεύτερης τάξης για την εύρεση του είδους των ακροτάτων στην ειδική περίπτωση δύο περιορισμών 
    και τριών μεταβλητών
    '''
    points_classification = []  # Λίστα με τα σημεία και το είδος του ακρότατου σε μορφή tuple

    # Αν τα δεσμευμένα κρίσιμα σημεία είναι μόνο ένα τότε το μετατρέπω σε λίστα
    if type(critical_points) == dict:
        critical_points = [critical_points]

    # Υπολογισμός των Εσσιανών πινάκων της συνάρτησης Lagrange στα δεσμευμένα κρίσιμα σημεία
    hessian_values = [hessian_matrix_value(lagrange_func_obj.lagrangian_hessian, point) for point in critical_points]
    
    for i, hessian in enumerate(hessian_values):
        determinant = np.linalg.det(hessian)
        if determinant > 0:
            points_classification.append((critical_points[i], 'local minimum'))
        elif determinant < 0:
            points_classification.append((critical_points[i], 'local maximum'))
        else:
            points_classification.append((critical_points[i], 'not a local optimizer'))

    return points_classification



        
    
    