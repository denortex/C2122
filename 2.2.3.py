class TransportnyiZasib:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Транспорт рухається зі швидкістю {self.speed} км/год"


class Avto(TransportnyiZasib):
    def move(self):
        return f"Автомобіль їде зі швидкістю {self.speed} км/год"


class Velosyped(TransportnyiZasib):
    def move(self):
        return f"Велосипед рухається зі швидкістю {self.speed} км/год"


class Litak(TransportnyiZasib):
    def move(self):
        return f"Літак летить зі швидкістю {self.speed} км/год"

print("\n=== Завдання 3 ===")
car = Avto(120)
bike = Velosyped(25)
plane = Litak(800)

print(car.move())
print(bike.move())
print(plane.move())
