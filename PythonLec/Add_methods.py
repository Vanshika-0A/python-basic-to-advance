class BankAccount:
    def __init__(self,owner,Account_no,balance):
        self.owner = owner
        self.account_number = Account_no
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self,withdraw):
        self.balance -= withdraw
        print(f"Withdrew {withdraw}. New balance: {self.balance}")
    def display(self):
        print(f"Account owner: {self.owner}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: {self.balance}")    
acc1 = BankAccount("Vanshika", "123456789", 1000)
acc1.deposit(500)
acc1.withdraw(200)
acc1.display()
acc2 = BankAccount("Anshika", "987654321", 2000)
acc2.deposit(1000)  
acc2.withdraw(500)
acc2.display()
