class Osoba:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    def __str__(self):
        return f"Особа: {self.name}, {self._age} років"


class Vodiy(Osoba):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number

    def __str__(self):
        return f"Водій: {self.name}, {self._age} років, посвідчення № {self.license_number}"


print("\n=== Завдання 2 ===")
person = Osoba("Олександр", 25)
driver = Vodiy("Іван", 30, "AB123456")

print(person)
print(driver)
