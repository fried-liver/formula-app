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