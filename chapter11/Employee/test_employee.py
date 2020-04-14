from employee import Employee
from unittest import TestCase, main

class TestEmployee(TestCase):
    def setUp(self):
        self.employee = Employee('Luis', 'Coelho', 20000)
            
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(25000, self.employee.annual_salary)
        
    def test_give_custom_raise(self):
        self.employee.give_raise(20000)
        self.assertEqual(40000, self.employee.annual_salary)


if __name__ == '__main__':
    main()