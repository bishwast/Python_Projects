class Account:
    """
    Account class that takes following 4 parameters
        1. Account Number
        2. Account Holder Name
        3. Current Balance
        4. Account Types - Includes 3 types of account types


    """
    def __init__(self, account_num, account_holder_name, current_balance, account_type = "Current, Savings, Investment"):
        """
        Instantiating the class Account.
        :param account_num: number
        :param account_holder_name: string
        :param current_balance: number
        :param account_type: 3 types, comma separated for each element
        """
        self.account_num = account_num
        self.account_holder_name = account_holder_name
        self.current_balance = current_balance
        self.account_type = account_type.split(', ')

    def __str__(self):
        """
        String representation of the Object of a class Account using __str__ method
        :return: String representation of the object based on what we specify in the __str__ method
        """
        # calling .join() method on a string ', ' so that strings can be concatenated  when a list of strings is passed
        # so can be displayed into a single string with comma separated values.
        account_types = ', '.join(self.account_type)
        return f"Account type/s: {account_types}"
    def deposit(self, amount):
        """
        Function that adds balance to the account parameter.
        :param amount: Takes in amount of any numeric values as a parameter
        :return: deposit amount, current balance
        """
        print(f"Account Number: {self.account_num}, Account Type: {', '.join(self.account_type)} \n" 
              f"Account Holder: {self.account_holder_name} \n"
              f"Current Balance: {self.current_balance} ")
        self.current_balance += amount
        return f"Deposit Amount: {amount}"

    def withdraw(self, amount):
        """
        Checks for current balance if greater than withdrawal amount.
        If condition is True returns existing balance and current balance.
        :param amount: Passed in once the function is called.
        :return: balance alert and balance.
        """
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
        """
        Grabs current balance of the account.
        :return: current balance
        """
        return self.current_balance

acc1 = Account("123", "Peter", 10000, "Current, Savings, Investment")
print(acc1.deposit(5000))
print("--"*50)
print(acc1.withdraw(500))
print("--"*50)
print("Outstanding Balance: ", acc1.get_balance())
print("**"*50)
acc2 = Account("345", "Mark", 1000, "Savings")
print(acc2.deposit(400))
print("--"*50)
print(acc2.withdraw(2000))
print("--"*50)
print("Outstanding Balance: ", acc2.get_balance())