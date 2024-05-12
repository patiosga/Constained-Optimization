from sympy import Symbol, Function
import helper_funcs as hf


# Description: This file contains the class definition for the lagrangian function
class lagrangian_func():
    def __init__(self, **kwargs):
        # Συνάρτηση f(x) που θέλουμε να βρουμε τα ακρότατα
        self.main_func: Function = kwargs['functions'][0]
        # Περιορισμοί g_i(x) = 0
        self.contraints: list[Function] = kwargs['functions'][1:]
        self.variables: list[Symbol] = kwargs['variables']
        
        # Προσθέτω τον πολλαπλασιαστή langrange στις μεταβλητές
        lambda_var = Symbol('lambda')
        self.variables.append(lambda_var)

        # Ορίζω την συνάρτηση lagrangian L(x, λ) = f(x) - Σ λ_i * g_i(x) για i = 1, 2
        if len(self.contraints) == 1:
            self.lagrangian = self.main_func - lambda_var * self.contraints[0]
        elif len(self.contraints) == 2:
            self.lagrangian = self.main_func - lambda_var * self.contraints[0] - lambda_var * self.contraints[1]
        else:
            raise ValueError('Η συνάρτηση Lagrange δέχεται μέχρι δύο περιορισμούς')
        
        # Υπολογισμός του ανάδελτα της συνάρτησης Lagrange
        self.lagrangian_gradient: list = hf.calc_gradient(self.lagrangian, self.variables)

        # Υπολογισμός του Εσσιανού της συνάρτησης Lagrange
        self.lagrangian_hessian: list[list] = hf.calc_hessian_matrix(self.lagrangian, self.variables)


    