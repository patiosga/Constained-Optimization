from helper_funcs import find_critical_points, sufficient_condition_second_grade
from lagrangian_func import lagrangian_func
from sympy import Symbol


def main_solver(main_func, constraints, variables):
    # Δημιουργώ το αντικείμενο της συνάρτησης Lagrange
    lagrange_obj = lagrangian_func(functions=[main_func, *constraints], variables=variables)
    print("Lagrange function: ", lagrange_obj.lagrangian)
    print("Hessian matrix: ", lagrange_obj.lagrangian_hessian)

    # Εύρεση των δεσμευμένων κρίσιμων σημείων
    critical_points = find_critical_points(lagrange_obj)

    # Εύρεση του είδους των ακροτάτων της συνάρτησης f(x) μετά την εύρεση των δεσμευμένων κρίσιμων σημείων
    points_classification = sufficient_condition_second_grade(lagrange_obj, critical_points)

    print("\nClassification of critical points: ")
    for point, classification in points_classification:
        final_str = "Critical point: "
        for var in point:
            if var != lagrange_obj.variables[-1]:  # Αφαιρώ τον πολλαπλασιαστή lagrange
                final_str += f'{var} = {point[var]}, '
        print(f'{final_str}Classification: {classification}')
