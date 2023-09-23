class Account:
    def __init__(self, account_num, account_holder_name, current_balance, account_type = ["current", "Savings", "Investment"]):
        self.account_num = account_num
        self.account_holder_name = account_holder_name
        self.current_balance = current_balance
        self.account_type = account_type

    def deposit(self, amount):
        print(f"Account Number: {self.account_num} \n"
              f"Existing balance: {self.current_balance}")
        self.current_balance += amount
        return f"Account Number: {self.account_num} \n" \
               f"Account Holder: {self.account_holder_name} \n" \
               f"Current balance: {self.current_balance}\n" \
               f"Account Type: {self.account_type}"

    def withdraw(self, amount):
        # existing balance
        print(f"Account Number: {self.account_num} has existing balance of {self.current_balance}")

        # check if the withdrawn amount is greater than the current balance,
        if self.current_balance < amount:
            print("Insufficient funds")
        else:
            self.current_balance -= amount
        # if amount less than current balance then withdraw, so current balance = current balance - amount
        return f"Account Number: {self.account_num} \n" \
               f"Withdraw amount: {amount}\n" \
               f"Current balance: {self.current_balance}"

    def get_balance(self):
        return self.current_balance

acc1 = Account("123", "Hann", 1000, ["Current"])
print(acc1.deposit(200))
print(acc1.withdraw(120))
print("Current Balance: ", acc1.get_balance())

