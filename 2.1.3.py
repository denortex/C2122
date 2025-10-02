class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостатньо коштів!")

    def __str__(self):
        return f"Рахунок {self.account_number} | Власник: {self.owner} | Баланс: {self.balance} грн"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
            else:
                print("Недостатньо коштів для переказу!")

    def show_accounts(self):
        for acc in self.accounts.values():
            print(acc)


a1 = BankAccount("Іван", "UA123", 1000)
a2 = BankAccount("Олена", "UA456", 500)

bank = Bank()
bank.add_account(a1)
bank.add_account(a2)

bank.show_accounts()
bank.transfer("UA123", "UA456", 300)
print("\nПісля переказу:")
bank.show_accounts()
