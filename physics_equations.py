import math
class final_velo:
    def __init__(self, V=None, u=None, a=None, s=None):
        super().__init__()
        self.V = V
        self.u = u
        self.a = a
        self.s = s
        self.var_dict = {"V": self.V, "u": self.u, "a": self.a, "s": self.s}
    
    def solve_V(self):
        V = math.sqrt(self.u**2+2*(self.a*self.s))
        return round(V, 1)
    
    def solve_u(self):
        u = math.sqrt(self.V**2 - 2*(self.a*self.s))
        return round(u, 1)

    def solve_a(self):
        a = (self.V**2 - self.u**2)/(2*self.s)
        return round(a, 1)
    
    def explanataion(self):
        if not self.V:
            self.var_dict.pop("V")
            self.explain("V", self.var_dict, "V² = u² + 2as", self.solve_V)
        elif not self.u:
            self.var_dict.pop("u")
            self.explain("u", self.var_dict, "V² = u² + 2as", self.solve_u, "u² = V² - 2as")
        elif not self.a:
            self.var_dict.pop("a")
            self.explain("a", self.var_dict, "V² = u² + 2as", self.solve_a, "a = (V² - u²)/2s")
        elif not self.s:
            self.var_dict.pop("s")
            self.explain("s", self.var_dict, "V² = u² + 2as", self.solve_a, "s = (V² - u²)/2a")
        
class wave_equation:
    def __init__(self, speed=None, wavelength=None, frequency=None):
        self.speed = speed
        self.wavelength = wavelength
        self.frequency = frequency

    def solve_speed(self):
        speed = self.wavelength * self.frequency
        return speed
    
    def solve_wavelength(self):
        wavelength = self.speed/self.frequency
        return wavelength
    
    def solve_frequency(self):
        frequency = self.speed/self.wavelength
        return frequency
    
solve = wave_equation(speed=2.5, wavelength=10, frequency=None)
print(solve.solve_frequency())
  
