class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Поповнено {amount} грн. Новий баланс: {self.balance} грн.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Знято {amount} грн. Залишок: {self.balance} грн.")
        else:
            print("Недостатньо коштів на рахунку!")

    def __str__(self):
        return f"Рахунок №{self.account_number} | Баланс: {self.balance} грн"

print("=== Завдання 1 ===")
acc = BankAccount("UA12345", 1000)
print(acc)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)
print(acc)
