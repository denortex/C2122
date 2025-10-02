class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary} грн"

print("\n=== Завдання 3 ===")
emp1 = Employee("Олена", "Менеджер", 25000)
emp2 = Employee("Ігор", "Програміст", 40000)

print(emp1.get_salary_info())
print(emp2.get_salary_info())
