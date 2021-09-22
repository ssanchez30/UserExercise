class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
        else:
            print("We cannot process your withdrawal.")
            print(f"You currently have {self.account_balance}.")
            print(f"And you are trying to withdraw {amount}.")

    def display_user_balance(self):
        print(f"Balance: {self.account_balance}")

    def validateFunds(self, amount):
        if self.account_balance > amount:
            return True
        else:
            return False

    def transfer_money(self, other_user, amount):
        if self.validateFunds(amount):
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
        else:
            print("You don't have enough funds to transfer.")
