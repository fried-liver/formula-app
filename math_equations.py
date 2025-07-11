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
        b=(-self.a*self.x**2-self.c)/self.x
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


class sine(Equation):
    def __init__(self, A=None, B=None, a=None, b=None):
        super().__init__()
        self.A = A
        self.B = B
        self.a = a
        self.b = b
        self.var_dict={"A":self.A, "B":self.B, "a":self.a, "b":self.b}
    def solve_A(self):
        A = math.asin((math.sin(math.radians(self.B))*self.a)/self.b)
        return round(math.degrees(A), 1)
    
    def solve_a(self):
        a = (self.b * math.sin(math.radians(self.A))/math.sin(math.radians(self.B)))
        return round(a, 1)
    def explanation(self):
        if not self.A:
            self.var_dict.pop("A")
            self.explain("A", self.var_dict, "sin(A)/a = sin(B)/b = sin(C)/c", self.solve_A, "A = sin⁻¹((sin(B)*a)/b)")
        if not self.B:
            self.var_dict.pop("B")
            self.explain("B", self.var_dict, "sin(A)/a = sin(B)/b = sin(C)/c", self.solve_A, "B = sin⁻¹((sin(A)*a)/a)")
        if not self.a:
            self.var_dict.pop("a")
            self.explain("a", self.var_dict, "sin(A)/a = sin(B)/b = sin(C)/c", self.solve_a, "a = (sin(A)*b)/sin(B)")
        if not self.b:
            self.var_dict.pop("b")
            
            self.explain("b", self.var_dict, "sin(A)/a = sin(B)/b = sin(C)/c", self.solve_a, "b = (sin(B)*a)/sin(A)")



class Cos_Rule(Equation):
    def __init__(self, x=None, a=None, b=None, c=None):
        super().__init__()
        self.x=x
        self.a=a
        self.b=b
        self.c=c
        self.var_dict={"x":self.x, "a":self.a, "b":self.b, "c":self.c}
    def solve_x(self):
        cos_A = (self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)
        return cos_A
    def solve_a(self):
        a=math.sqrt(self.b**2+self.c**2-2*self.b*self.c*math.cos(self.x))
        return a      
    def solve_b(self):

        b=self.a*math.cos(self.x)+math.sqrt(self.c**2-self.a**2*math.cos(self.x)**2)
        return b
    def solve_c(self):
        c=self.a*math.cos(self.x)+math.sqrt(self.b**2-self.a**2*math.cos(self.x)**2)
        return c
    
            
    def cos_explanation(self):
        if not self.x:
            self.var_dict.pop("x")
            self.explain("x", self.var_dict, "a^2 = b^2 + c^2 - 2bc cos(X)", self.solve_x, "cos(X) = (b^2 + c^2 - a^2) / 2bc")
        elif not self.a:
            self.var_dict.pop("a")
            self.explain("a", self.var_dict, "a^2 = b^2 + c^2 - 2bc cos(X)", self.solve_x, "a = sqrt(b^2 + c^2 - 2bc cos(X))")
        elif not self.b:
            self.var_dict.pop("b")
            self.explain("b", self.var_dict, "a^2 = b^2 + c^2 - 2bc cos(X)", self.solve_x, "b = a cos(C) ± √(c² - a² + a² cos²(x))")
        elif not self.c:
            self.var_dict.pop("c")
            self.explain("c", self.var_dict, "a^2 = b^2 + c^2 - 2bc cos(X)", self.solve_x, "c = a cos(x) ± √(b² - a² + a² cos²(x))")
        
        