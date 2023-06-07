class BankAccount:
    All_accounts = []
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.All_accounts.append(self)
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
        
    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * (self.int_rate))
        return self
    
    @classmethod
    def bank_account_info(cls):
        for account in cls.All_accounts:
            print(account.balance)

td = BankAccount(0.01, 1000)
td.display_account_info().deposit(200).deposit(50).deposit(100).withdraw(500).yield_interest().display_account_info()

chase = BankAccount(0.15, 500)
chase.display_account_info().deposit(100).deposit(200).deposit(100).withdraw(100).yield_interest().display_account_info()

BankAccount.bank_account_info()