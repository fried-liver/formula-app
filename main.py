def main_screen():
 """
 1. Math
 2. Physics
 3. Quit
"""
def physics_equation():
 """
1. Wave 
2. Half Life
3. Final Velocity
"""
def math_equation():
 """
 1. Quadratic equation
 2. Sine rule
 3. Cosine rule
"""

"""for i in len(math_menu):
    print(i + "." m " " + ath)_menu[i]"""

print("Archimedes  1.0.\n Welcome to MIST’s greatest equations solver ever! ☆*: .｡. o(≧▽≦)o .｡.:*☆\n")
main_menu = input("Please choose one of the options  (^^)\n ")
main_menu_2 = input("Please enter a number:   ")
while main_menu != 3:
    print(main_menu)
    print(main_screen)
    if main_menu == 1:
        match main_menu:
            case 1:
                [print(math_equation())]
                [print(main_menu_2)]
            case 2:
                [print(physics_equation())]
                [print(main_menu_2)]  
    else:
        break
    if main_menu_2 == 1:
       match main_menu_2:
          case 1:
             [print(Quadratic_equation())]
             
        

