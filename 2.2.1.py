class Tvarina:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "Тварина видає звук"

    def __str__(self):
        return f"{self.name}, {self.age} років"


class Sobaka(Tvarina):
    def sound(self):
        return "Гав-гав!"


class Kit(Tvarina):
    def sound(self):
        return "Мяу-мяу!"


print("=== Завдання 1 ===")
dog = Sobaka("Рекс", 3)
cat = Kit("Мурчик", 2)

print(dog, "-", dog.sound())
print(cat, "-", cat.sound())
