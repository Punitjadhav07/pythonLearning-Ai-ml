# 1. Class & Object (Basic, but people mess this up)

# Task:
# Build a BankAccount class.

# Requirements:

# Attributes: owner, balance
# Methods:
# deposit(amount)
# withdraw(amount) (block if insufficient funds)
# display_balance()

# Twist (important):

# Prevent negative deposits
# Track total number of transactions



class BankAccount :
    def __init__ (self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.__transactions = 0 

    def deposit(self,amount):
        if amount < 0:
            print ("negative deposits are not allowed")
        else:
            self.__balance+= amount
            self.transactions += 1
    
    def withdraw(self,amount):
        if amount > self.balance:
            print ("insufficient funds")
        else:
            self.__balance -= amount
            self.__transactions += 1
    def display_balance(self):
        print (f"{self.owner} has a balance of {self.balance}")
        
punit = BankAccount("Punit",-1000)
punit.deposit(-500)
punit.withdraw(200)
punit.display_balance() 
print(punit.transactions) 
