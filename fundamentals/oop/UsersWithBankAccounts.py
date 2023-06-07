class BankAccount:
    Accounts = []
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.Accounts.append(self)
        
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
        for account in cls.Accounts:
            print(account.balance)


class User:
    def __init__(self, name, email, BankAccount):
        self.name = name
        self.email = email
        self.bank = BankAccount
    
    def make_withdrawal(self, amount):
        self.bank.withdraw(amount)
        print(self.bank.balance)
    
    def make_deposit(self, amount):
        self.bank.deposit(amount)
        print(self.bank.balance)
        
    def display_user_balance(self):
        self.bank.display_account_info()


chase = BankAccount(0.02, 500)
td = BankAccount(0.02, 1000)
yancie = User("Yancie", "yancie@gmail.com", td)
yancie2 = User("Yancie", "yancie@gmail.com", chase)
yancie.make_deposit(100)
yancie.make_withdrawal(200)
yancie.display_user_balance()








# yancie.bank.bank_account_info()
# td.display_account_info().deposit(200).deposit(50).deposit(100).withdraw(500).yield_interest().display_account_info()

# print(Yancie_account.name)
# td.display_account_info().deposit(200).deposit(50).deposit(100).withdraw(500).yield_interest().display_account_info()


# chase.display_account_info().deposit(100).deposit(200).deposit(100).withdraw(100).yield_interest().display_account_info()

# BankAccount.bank_account_info()
