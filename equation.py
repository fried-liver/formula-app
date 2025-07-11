

class Equation:
    def __init__(self):
        pass
    def replace(self, string, dict_):
        new_str=""
        
        for i in range(len(string)):
    
            if string[i] in dict_:
                new_str+="("+str(dict_[string[i]])+")"
            else:
                new_str+=string[i]
            

    
        return new_str
    def explain(self, solve_var, var_dict, equation, solve_func, subject_equation=None, ):
        print(f"To solve for {solve_var}, enter the values into the equation: ")
        print(equation)
        print(self.replace(equation, var_dict))
        if subject_equation:
            print(f"make {solve_var} the subject")
            print(subject_equation)
            print(self.replace(subject_equation, var_dict))
        print(f"The answer is {solve_func()}")

