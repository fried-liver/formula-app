from math_equations import *
def math_menu():
    math_menu = [
        "Quadratic equation",
        "Sine rule",
        "Cosine rule"]

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

if __name__=="__main__":
    pass