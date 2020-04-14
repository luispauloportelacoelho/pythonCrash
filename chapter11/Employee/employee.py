class Employee:
    def __init__(self, firs_name, last_name, annual_salary):
        self.firs_name = firs_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, value=None):
        if value is None:
            self.annual_salary += 5000
        else:
            self.annual_salary += value
        return self.annual_salary
            