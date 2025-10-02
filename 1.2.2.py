class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"[{self.year}] {self.make} {self.model}"

print("\n=== Завдання 2 ===")
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("BMW", "X5", 2022)

print(car1.get_info())
print(car2.get_info())
