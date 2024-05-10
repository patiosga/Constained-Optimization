from sympy import symbols, diff, Function, Matrix, hessian


# Description: This file contains the class definition for the lagrangian function
class lagrangian_func():
    def __init__(self, **kwargs):
        self.main_func = kwargs['funcs'][0]
        self.contraints: list = kwargs['funcs'][1:]
        self.variables = kwargs['variables']
        self.lagrangian = None
        self.lagrangian_gradient = None
        self.lagrangian_hessian = None
        self.lagrangian_multipliers = None

    def calc_lagrangian(self):
        pass
    

    def calc_lagrangian_gradient(self):
        pass


    def calc_lagrangian_hessian(self):
        pass


    