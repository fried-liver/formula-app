physics_menu = [
    "1. Wave Equation",
    "2. Half life",
    "3. Final Velocity"]

for i in range(len(physics_menu)):
    print(str(i+1) + "." + " " + physics_menu[i])

choice = input("Please enter a number: ")

try:
    choice = int(choice)
    if 1 <= choice <= len(physics_menu):
        print(f"You selected: {physics_menu[choice - 1]}")
    else:
        print("Invalid choice. Please select a number from the list.")
except ValueError:
    print("Invalid input. Please enter a number.")
    
