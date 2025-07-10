import math
class Quadratic:
    def __init__(self, x=None, a=None, b=None, c=None):
        self.x=x
        self.a=a
        self.b=b
        self.c=c

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
            print("To solve for x, enter the values in the quadratic formula: ")
            print(f"(-b ± sqrt(b^2 - 4ac)) / 2a")
            print(f"(-{self.b} ± sqrt({self.b}^2 - 4*{self.a}*{self.c})) / 2*{self.a}")
            print(self.solve_x())
        elif not self.a:
            print("To solve for a, enter the values into the equation: ")
            print("ax^2 + bx + c = 0")
            print(f"a*{self.x}^2 + {self.b}*{self.x} + {self.c} = 0")
            print(f"make a the subject")
            print("a = (-c-bx) / x^2")
            print(f"")

q=Quadratic(x=None, a=2, b=2, c=0)
print(q.solve_x())
