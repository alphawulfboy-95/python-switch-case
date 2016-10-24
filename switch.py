"""
An implementation of switch-case structures in Python 3
by Nicholas Lau Kheng Seng (email: nicho.lau95@gmail.com)
"""

class Case(object):
    def __init__(self, value, function=None, breaker = False):
        self.value = value        # value the variable has to match in order to execute the method
        self.method = function    # the function (now a method) executed when the value matches the variable
        self.breaker = breaker    # if true, stops the switch-case statement from continueing

class Switchable(object):
    def __init__(self, variable, *cases):
        self.variable = variable  # the variable you are testing
        self.cases = list(cases)  # a list of Case objects
    def set_variable(self, variable):
        self.variable = variable  # changes the variable to be checked
    def add_case(self, case):
        self.cases.append(case)   # adds a new case
    def switch(self):
        start = False
        for case in self.cases:
            if case.value == self.variable:
                start = True
            if start == True:     # runs each method after a match found until case.breaker == True
                if callable(case.method):
                    case.method() # calls the method
                if case.breaker:
                    break         # breaks when case.breaker is true.

# function for quick usage
def switch(variable, *cases):
    temp = Switchable(variable)   # unfortunately, putting in the cases tuple as an argument would make temp.cases = ((cases))
    for case in cases:
        temp.add_case(case)
    temp.switch()
    del temp

# example use
if __name__ == "__main__":
    def func0():
        print("variable is value 0")
        
    case0 = Case(0, func0)
    
    def func1():
        print("1+1="+(str(1+1)))
        
    case1 = Case(1,func1, breaker = True)
    
    case2 = Case(2,breaker = True)
    
    def func2():
        print("The end!")
        
    case3 = Case(3, func2)
    
    for n in range(4):
        print("n = " + str(n))
        switch(n, case0,case1,case2,case3)
        print("")
