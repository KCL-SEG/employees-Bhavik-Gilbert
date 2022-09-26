"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, hours, rate, contracts, contract_rate):
        self.name = name
        self.hours = hours
        self.rate = rate
        self.contracts = contracts
        self.contract_rate = contract_rate

    def get_pay(self):
        hours = self.hours
        contracts = self.contracts

        if self.hours < 0:
            hours = 1
        if self.contracts <= 0:
            contracts = 1
        
        return (self.rate * hours) + (contracts * self.contract_rate)

    def __str__(self):
        pay = ""
        base = 0

        if(self.hours < 0):
            pay += f"{self.name} works on a monthly salary of {self.rate}"
        else:
            pay += f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour"

        if(self.contracts == 0 and self.contract_rate > 0):
            pay += f" and receives a bonus commission of {self.contract_rate}"
        elif(self.contracts > 1):
            pay += f" and receives a commission for {self.contracts} contract(s) at {self.contract_rate}/contract"

        pay += f".  Their total pay is {self.get_pay()}."
        
        print(pay)
        return pay


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', -1, 4000, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 100, 25, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', -1, 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', -1, 2000, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 120, 30, 0, 600)
