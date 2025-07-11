import math_equations
math_menu = [
    "Quadratic equation",
    "Sine rule",
    "Cosine rule"]

physics_menu = [
    "Wave Equation",
    "Half life",
    "Final Velocity"]

def main_screen():
    main_screen = """
    1. Math
    2. Physics
    3. Quit
    """
    return main_screen

def is_int(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def get_int():
    while True:
        int_input = input("Enter integer: ")
        if is_int(int_input):
            return int(int_input)
        else:
            print("Input must be integer. Please re enter")

print("Archimedes  1.0.\n Welcome to MIST's greatest equations solver ever! ☆*: .｡. o(≧▽≦)o .｡.:*☆\n")
ask = "Please choose one of the options  (^^)\n"
while True:
    print(main_screen())
    print(ask)
    resp = int(get_int())
    
    print(resp)
    if resp == 1:
        for i in range(len(math_menu)):
            print(str(i+1) + "." + " " + math_menu[i])
        while True:
            try:
                choice = int(input("Please enter a number: "))
                if 1 <= choice <= len(math_menu):
                    #math_equations.math_equation(math_menu[choice - 1])
                    print(f"You selected: {math_menu[choice - 1]}")
                    break
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input, please enter a number.")
                if choice == 1:
                    pass
    if resp == 2:
        for i in range(len(physics_menu)):
            print(str(i+1) + "." + " " + physics_menu[i])

        choice = input("Please enter a number: ")
        while choice == None:
            try:
                choice = int(choice)
                if 1 <= choice <= len(physics_menu):
                    print(f"You selected: {physics_menu[choice - 1]}")
                else:
                    print("Invalid choice. Please select a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

"""
        elif resp == 2:
            print(physics_option())
            print(resp2)
        elif resp == 3:
            break
        else:
            print("Not a valid number")
                break
"""

"""
   if resp2 == 1:
       print(Quadratic_equation())
    elif resp2 == 2:
       print(Sine_Rule_equation())
    elif resp2 == 3:
       print(Cosine_Rule_equation())
"""
main()

