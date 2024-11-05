class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        total = sum(emp.salary for emp in self.employees)
        return total

# Example usage
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
payroll = Payroll()
payroll.add_employee(emp1)
payroll.add_employee(emp2)
print("Total Payroll:", payroll.calculate_total_payroll())
