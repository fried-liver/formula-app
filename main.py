from math_menu import math_menu
from validation import get_int, get_float
from physics_menu import physics_menu

def main():
    menu_ = """
        1. Math
        2. Physics
        3. Quit
        """
    while True:
        print(menu_)
        resp = int(get_int())
        print(resp)
        if resp == 1:
            math_menu()
        elif resp == 2:
            physics_menu()
        elif resp == 3:
            print("Thank you for using!")
            break
        else:
            print("Not a valid number")

"""
   if choice == 1:
       print(Quadratic_equation())
    elif choice == 2:
       print(Sine_Rule_equation())
    elif choice == 3:
       print(Cosine_Rule_equation())

    if choice == 1:
        print(Wave_equation())
        elif choice == 2:
        print(Half_Life_equation())
        elif choice == 3:
        print(Final_Velocity_equation())
"""
main()

