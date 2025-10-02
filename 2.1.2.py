class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        return f"{self.name} | {self.price} грн | {'В наявності' if self.available else 'Немає'}"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product.available:
            self.items.append(product)
        else:
            print(f"Товар {product.name} недоступний!")

    def remove_product(self, name):
        self.items = [p for p in self.items if p.name != name]

    def total_price(self):
        return sum(p.price for p in self.items)

    def show_cart(self):
        if not self.items:
            print("Кошик порожній.")
        else:
            for p in self.items:
                print(p)
            print(f"Загальна сума: {self.total_price()} грн")


p1 = Product("Ноутбук", 25000)
p2 = Product("Мишка", 500)
p3 = Product("Навушники", 2000, available=False)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.show_cart()
