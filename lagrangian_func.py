from sympy import Symbol, Function
import helper_funcs as hf


class lagrangian_func():
    '''
    Κλάση που αναπαριστά την συνάρτηση Lagrange για το πρόβλημα της βελτιστοποίησης με περιορισμούς.
    Είναι απόλυτα scalable υπό την έννοια ότι μπορεί να δεχτεί οποιοδήποτε πλήθος ισοτικών περιορισμών και ορίζεται κανονικά.
    '''
    def __init__(self, **kwargs):
        # Συνάρτηση f(x) που θέλουμε να βρουμε τα ακρότατα
        self.main_func: Function = kwargs['functions'][0]
        # Περιορισμοί g_i(x) = 0
        self.contraints: list[Function] = kwargs['functions'][1:]
        self.variables: list[Symbol] = kwargs['variables']
        
        # Προσθέτω τον πολλαπλασιαστές langrange στις μεταβλητές
        if len(self.contraints) == 0:
            raise ValueError('No constraints given')
        elif len(self.contraints) == 1:
            lambdas = [Symbol('lambda')]
            self.variables.append(lambdas[0])
        else:
            lambdas = [Symbol('lambda' + f'{i+1}') for i in range(len(self.contraints))]
            for temp_lambda in lambdas:
                self.variables.append(temp_lambda)

        # Ορίζω την συνάρτηση lagrangian L(x, λ) = f(x) - Σ λ_i * g_i(x) για i = 1, 2, ...
        self.lagrangian: Function = self.main_func - sum([lambdas[i] * g for i, g in enumerate(self.contraints)])
    
        # Υπολογισμός του ανάδελτα της συνάρτησης Lagrange
        self.lagrangian_gradient: list = hf.calc_gradient(self.lagrangian, self.variables)

        # Υπολογισμός του Εσσιανού της συνάρτησης Lagrange
        self.lagrangian_hessian: list[list] = hf.calc_hessian_matrix(self.lagrangian, self.variables)


    