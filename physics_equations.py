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
  


if __name__=="__main__":
    pass
