import math_equations
math_menu = [
    "Quadratic equation",
    "Sine rule",
    "Cosine rule"]

physics_menu = [
    "Wave Equation",
    "Half life",
    "Final Velocity"]

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

def main():
    menu_ = """
        1. Math
        2. Physics
        3. Quit
        """
    while True:
        print("Archimedes  1.0.\n Welcome to MIST's greatest equations solver ever! ☆*: .｡. o(≧▽≦)o .｡.:*☆\n")
        print(menu_)
        print = "Input Option: "
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

        if resp == 3:
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
"""
main()

