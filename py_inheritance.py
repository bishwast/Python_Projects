class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print(f"Happy birthday {self.name}, your were {self.age} years old.")
        self.age +=1
        print(f"{self.name} you are now {self.age} years old.")

"""
# Following code can be used if we want to print an instance of
Person class without calling the birthday() method.  
    def __str__(self):
        return f"{self.name} is {self.age} years old."
"""


# Inheriting the Person class
class Employee(Person):
    def __init__(self, name, age, id):
        # Initializing instances of the class with super().__init_() reference.
        super().__init__(name, age)
        self.id = id

# Additional behavior of the Employee Class.
    def calculate_pay(self,hours_worked):
        hourly_rate = 9.50
        if self.age> 21:
            hourly_rate +=2.50
        total_pay = hourly_rate * hours_worked
        return total_pay

# Subclass : Subclassing Employee with a new class.
class SalesPerson(Employee):
    def __init__(self, name, age, id, region, sales):
        # Initializing attributes from parent class Employee
        super().__init__(name, age, id)
        self.region = region
        self.sales = sales

# New behavior of the subclass SalesPerson.
    def bonus(self):
        return f"Your bonus is {self.sales * 0.50}"

"""
Notes: 
Now class SalesPerson has attributes name, age, id, in addition to 
region and sales. It also inherits birthday() and calculate_pay() 
behaviors and has its own bonus() behavior. 
The logic behind subclass is 
SalesPerson.__init__() method calls Employee.__init__() method.
"""

print("From Class Person")
p = Person("Henry", 35)
p.birthday()
print("**" * 25)

print("From Class Employee")
e = Employee("John", 32, 1221)
e.birthday()
print(f"Pay (e.Calculate_pay(40)): {e.calculate_pay(40)}")
print("**"*25)

print("From SubClass SalesPerson")
sp = SalesPerson("Peter", 25, 2332, "North America", 500)
sp.birthday()
print(f"Pay: {sp.calculate_pay(40)}")
print(f"Bonus: {sp.bonus()}")