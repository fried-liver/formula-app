import math
from equation import Equation


class Quadratic(Equation):
    def __init__(self, x=None, a=None, b=None, c=None):
        super().__init__()
        self.x=x
        self.a=a
        self.b=b
        self.c=c
        self.var_dict={"x":self.x, "a":self.a, "b":self.b, "c":self.c}
    def solve_x(self):
        disc=self.b**2-4*self.a*self.c
        if disc>=0:
            x1=(-self.b+math.sqrt(disc))/(2*self.a)
            x2=(-self.b-math.sqrt(disc))/(2*self.a)
        else:
            pass
        
        return x1, x2
    def solve_a(self):
        
        a=(-self.b*self.x-self.c)/self.x**2
        return a
    def solve_b(self):
        b=(-self.a*self.x^2-self.c)/self.x
        return b
    def solve_c(self):
        c=-self.a*self.x**2-self.b*self.x
        return c
    def explanation(self):
        if not self.x:
            
            self.var_dict.pop("x")
            self.explain("x", self.var_dict, "x = (-b ± sqrt(b^2 - 4ac)) / 2a", self.solve_x) 
        elif not self.a:
        
            self.var_dict.pop("a")
            self.explain("a", self.var_dict, "ax^2 + bx + c = 0", self.solve_a, "a = (-c-bx) / x^2") 
        elif not self.b:
            self.var_dict.pop("b")
            self.explain("b", self.var_dict, "ax^2 + bx + c = 0", self.solve_a, "b = (-c - ax^2) / x") 
        elif not self.c:
            self.var_dict.pop("c")
            self.explain("c", self.var_dict, "ax^2 + bx + c = 0", self.solve_a, "c = -ax^2 - bx") 


class sine:
    def __init__(self, A=None, B=None, a=None, b=None):
        self.A = A
        self.B = B
        self.a = a
        self.b = b
    
    def solve_A(self):
        A = math.asin((math.sin(math.radians(self.B))*self.a)/self.b)
        return round(math.degrees(A), 1)
    
    def solve_a(self):
        a = (self.b * math.sin(math.radians(self.A))/math.sin(math.radians(self.B)))
        return round(a, 1)

solve = sine(A=26.6, B=43, a=None, b=3.5)
print(solve.solve_a())
