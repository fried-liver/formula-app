def physics_menu():
    physics_menu = [
        "Wave Equation",
        "Half life",
        "Final Velocity"]

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
    


if __name__=="__main__":
    pass