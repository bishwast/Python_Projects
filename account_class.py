class Account:
    def __init__(self, account_num, account_holder_name, current_balance, account_type = "Current, Savings, Investment"):
        self.account_num = account_num
        self.account_holder_name = account_holder_name
        self.current_balance = current_balance
        self.account_type = account_type.split(', ')

    def __str__(self):
        # calling .join() method on a string ', ' so that strings can be concatenated  when a list of strings is passed
        # so can be displayed into a single string with comma separated values.
        account_types = ', '.join(self.account_type)
        return f"Account type/s: {account_types}"
    def deposit(self, amount):
        print(f"Account Number: {self.account_num}, Account Type: {', '.join(self.account_type)} \n" 
              f"Account Holder: {self.account_holder_name} \n"
              f"Current Balance: {self.current_balance} ")
        self.current_balance += amount
        return f"Deposit Amount: {amount}"

    def withdraw(self, amount):
        print(f"Account Number: {self.account_num}, Account Type: {', '.join(self.account_type)} \n" 
              f"Account Holder: {self.account_holder_name} \n"
              f"Current Balance: {self.current_balance}")
        # check if the withdrawn amount is greater than the current balance,
        if self.current_balance < amount:
            print("Insufficient funds")
        else:
            self.current_balance -= amount
        # if amount less than current balance then withdraw, so current balance = current balance - amount
        return f"Withdraw amount: {amount}\n"

    def get_balance(self):
        return self.current_balance

acc1 = Account("123", "Han", 1000, "Current, Savings")
print(acc1.deposit(200))
print("--"*50)
print(acc1.withdraw(120))
print("--"*50)
print("Outstanding Balance: ", acc1.get_balance())

