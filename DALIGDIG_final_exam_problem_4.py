# Parent Class
class Account():
    balance = None
    holder = None

    def __init__(self, account_holder, balance):
        self.balance = balance
        self.holder = account_holder 

    def deposit(self, amount):
        self.balance += amount 
        return self.balance 

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"

        self.balance -= amount 
        return self.balance    

# Child Class 
class CheckingAccount(Account):
# A bank account that charges for withdrawals.
    withdraw_charge = 10

    def __init__(self, withdraw_charge , account_holder, balance):
        self.withdraw_charge = withdraw_charge
        Account.__init__(self, account_holder, balance)

    def withdraw(self, amount):

        if amount > self.balance:
            return "Insufficient funds"
        amount += self.withdraw_charge
        self.balance -= amount   
        return self.balance
        
# when you withdraw, amount plus withdraw_charge will be subtracted from the account balance

# Child Class 
class SavingsAccount(Account):
# A bank account that charges for deposits.
    deposit_charge = 0

    def __init__(self, deposit_charge, account_holder, balance):
        self.deposit_charge = deposit_charge
        Account.__init__(self, account_holder, balance)
    
    def deposit(self, amount):
        amount -= self.deposit_charge 
        self.balance += amount
        return self.balance


# when you deposit, amount minus the deposit_charge will be the added to the account balance 

# Grandchild class 
class CustomerAccount(SavingsAccount, CheckingAccount):  
    def __init__(self, account_holder, balance, deposit_charge, withdraw_charge):
        SavingsAccount.__init__(self, deposit_charge, account_holder, balance)
        CheckingAccount.__init__(self, withdraw_charge , account_holder, balance)
    

if __name__ == "__main__":

    j = CustomerAccount("Juan", 500, deposit_charge = 0, withdraw_charge = 10)
    print(j.deposit(2000))
    print(j.withdraw(500))