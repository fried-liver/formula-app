math_menu = [
    "Quadratic equation",
    "Sine rule",
    "Cosine rule"]

for i in range(len(math_menu)):
    print(str(i+1) + "." + " " + math_menu[i])

choice = input("Please enter a number: ")

try:
    choice = int(choice)
    if 1 <= choice <= len(math_menu):
        print(f"You selected: {math_menu[choice - 1]}")
    else:
        print("Invalid choice. Please select a number from the list.")
except ValueError:
    print("Invalid input. Please enter a number.")
    