class Person:
    def __init__(self):
        self.name = input("Enter the name: ")
        self.gender = input("Enter the gender (m/f): ")
        self.phone = input("Enter the contact number: ")


class Loan(Person):
    def __init__(self):
        super().__init__()
        self.amt = int(input("Enter the loan amount: "))
        self.rate = float(input("Enter the interest rate: "))
        self.period = int(input("Enter the loan period (years): "))

    def calculate(self):
        si = (self.amt*self.rate*self.period)/100
        if(self.gender.lower() == 'm'):
            print(f"Hello Mr. {self.name} \nYour Interest is {si}")
        else:
            print(f"Hello Ms. {self.name} \nYour Interest is {si}")


l = Loan()
l.calculate()
