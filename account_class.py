class Account:
    def __init__(self, account_num, account_holder_name, current_balance, account_type = ["current", "Savings", "Investment"]):
        self.account_num = account_num
        self.account_holder_name = account_holder_name
        self.current_balance = current_balance
        self.account_type = account_type

    def deposit(self, amount):
        print(f"Your existing balance is {self.current_balance}")
        self.current_balance += amount
        return self.account_holder_name + f" for account number {self.account_num} has a current balance of {self.current_balance}"

    def withdraw(self, amount):
        print(f"Your existing balance is {self.current_balance}")
        # existing balance
        # check if the withdraw amount is greater than the current balance,
        # if amount less than current balance then withdraw, so current balance = current balance - amount

        return self.account_holder_name + f" for account number {self.account_num} has a balance of " + str(self.current_balance - self.withdraw())

    def get_balance(self):
        return self.current_balance

acc1 = Account("123", "Hann", 10.5, "Current")

