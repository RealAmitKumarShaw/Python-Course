class Employee:
    company = "TCS"

    def get_salary(self):       # self is important to access attributes and methods inside class
        print(self)
        return 34000
    
e1 = Employee()     # An object of a class Employee is created here
print(e1.company)   # TCS
print(e1.get_salary())  # 34000

e2 = Employee()
print(e2.get_salary())
