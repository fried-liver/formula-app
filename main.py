def main_screen():
 main_screen = """
 1. Math
 2. Physics
 3. Quit
"""
def physics_option():
 physics_option = """
1. Wave 
2. Half Life
3. Final Velocity
"""
def math_option():
 math_option = """
 1. Quadratic equation
 2. Sine rule
 3. Cosine rule
"""
def Quadratic_equation():
   Quadratic_equation = """

"""
def Sine_Rule_equation():
   Sine_Rule_equation = """

"""
def Cosine_Rule_equation():
   Cosine_Rule_equation = """

"""

print("Archimedes  1.0.\n Welcome to MIST’s greatest equations solver ever! ☆*: .｡. o(≧▽≦)o .｡.:*☆\n")
resp = input("Please choose one of the options  (^^)\n ")
resp2 = input("Please enter a number:   ")
while True:
    print(main_screen)
    print(resp)
    if resp == 1:
        print(math_option())
        print(resp2)
    elif resp == 2:
        print(physics_option())
        print(resp2)
    elif resp ==3:
        break
    else:
            print("Not a valid number")
    if resp2 == 1:
       print(Quadratic_equation())
    elif resp2 == 2:
       print(Sine_Rule_equation())
    elif resp2 == 3:
       print(Cosine_Rule_equation())
             
        

