"""def physics_menu():
    physics_menu = [
        "Wave equation",
        "Half-life equation",
        "Final velocity equation"]

    for i in range(len(physics_menu)):
        print(str(i+1) + "." + " " + physics_menu[i])

    while True:
        
        try:
            choice = int(input("Please enter a number: "))
            if 1 <= choice <= len(physics_menu):
                #physics_equations.math_equation(physics_menu[choice - 1])
                print(f"You selected: {physics_menu[choice - 1]}")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")"""

import validation
import physics_equations

def physics_menu():
    physics_menu = {
        1 : {
            "function" : physics_equations.wave_equation(),
            "variables" : ["speed", "wavelength", "frequency"],
        },
        2 : {
            "function" : physics_equations.final_velo(),
            "variables" : [""],
        },
    }

    for key in physics_menu.keys():
        print(key)
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 >= choice and choice <= len(physics_menu):
                for i in physics_menu[choice]["variables"]:
                    print(i)


        except ValueError:
            print("Invalid input")

physics_menu()
