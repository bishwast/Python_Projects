class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print(f"Happy birthday {self.name}, your current age is {self.age}.")
        self.age +=1
        print(f"{self.name} you are {self.age} years old.")

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


