class Employee:
    def calculate_salary(self):
        print("Calculating salary for employee...")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating salary for manager with additional bonuses...")

# Example usage
employee = Employee()
manager = Manager()
employee.calculate_salary()
manager.calculate_salary()
