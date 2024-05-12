from helper_funcs import find_critical_points, sufficient_condition_second_grade_one_constraint, sufficient_condition_second_grade_two_constraints
from lagrangian_func import lagrangian_func
from sympy import Symbol


def main_solver_one_constraint(main_func, constraints, variables):
    # Δημιουργώ το αντικείμενο της συνάρτησης Lagrange
    lagrange_obj = lagrangian_func(functions=[main_func, *constraints], variables=variables)
    print("Lagrange function: ", lagrange_obj.lagrangian)
    print("Hessian matrix: ", lagrange_obj.lagrangian_hessian)

    # Εύρεση των δεσμευμένων κρίσιμων σημείων
    critical_points = find_critical_points(lagrange_obj)

    # Εύρεση του είδους των ακροτάτων της συνάρτησης f(x) μετά την εύρεση των δεσμευμένων κρίσιμων σημείων
    points_classification = sufficient_condition_second_grade_one_constraint(lagrange_obj, critical_points)

    print_solution(lagrange_obj, points_classification)


def main_solver_two_constraints(main_func, constraints, variables):
    '''
    Επεκτάσεις του αλγορίθμου για δύο περιορισμούς στην ειδική περίπτωση όπου η main_func είναι συνάρτηση τριών μεταβλητών
    '''
    lagrange_obj = lagrangian_func(functions=[main_func, *constraints], variables=variables)
    print("Lagrange function: ", lagrange_obj.lagrangian)
    print("Hessian matrix: ", lagrange_obj.lagrangian_hessian)

    # Εύρεση των δεσμευμένων κρίσιμων σημείων
    critical_points = find_critical_points(lagrange_obj)

    # Εύρεση του είδους των ακροτάτων της συνάρτησης f(x) μετά την εύρεση των δεσμευμένων κρίσιμων σημείων
    points_classification = sufficient_condition_second_grade_two_constraints(lagrange_obj, critical_points)

    print_solution(lagrange_obj, points_classification)



def print_solution(lagrange_obj, points_classification):
    num_of_constraints = len(lagrange_obj.contraints)
    proper_vars = set(lagrange_obj.variables[:len(lagrange_obj.variables) - num_of_constraints])

    print("\nClassification of critical points: ")
    for point, classification in points_classification:
        final_str = "Critical point: "
        for var in point:
                if var in proper_vars:
                    final_str += f'{var} = {point[var]}, '
        print(f'{final_str}Classification: {classification}')
