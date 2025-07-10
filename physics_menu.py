phy_menu = [
    "Wave equation",
    "Half life",
    "Final velocity"]

for i in range(len(phy_menu)):
    print(str(i+1) + "." + " " + phy_menu[i])

choice = input("Please enter a number: ")

try:
    choice = int(choice)
    if 1 <= choice <= len(phy_menu):
        print(f"You selected: {phy_menu[choice - 1]}")
    else:
        print("Invalid choice. Please select a number from the list.")
except ValueError:
    print("Invalid input. Please enter a number.")
    