import math
class final_velo:
    def __init__(self, V=None, u=None, a=None, s=None):
        self.V = V
        self.u = u
        self.a = a
        self.s = s
    
    def solve_V(self):
        V = math.sqrt(self.u**2+2*(self.a*self.s))
        return round(V, 1)
    
    def solve_u(self):
        u = math.sqrt(self.V**2 - 2*(self.a*self.s))
        return round(u, 1)

    def solve_a(self):
        a = (self.V**2 - self.u**2)/(2*self.s)
        return round(a, 1)