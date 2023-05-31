class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to the bank")
 
    def deposit(self):
        amount=float(input("Enter amount to Deposit: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to Withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 

# creating an object of class
a = Bank_Account()
  
# Calling functions with that class object
a.deposit()
a.withdraw()
a.display()