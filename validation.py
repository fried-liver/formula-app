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

def is_float(user_input):
    try:
        float(user_input)
        return True
    except ValueError:
        return False

def get_float():
    while True:
        float_input = input("Enter float: ")
        if is_float(float_input):
            return float(float_input)
        else:
            print("Input must be float. Please re enter.")

get_float()


