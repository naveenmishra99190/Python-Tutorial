#Encapsulation : Protect data inside a class

class Account:
    def __init__(self, bal, acc):
        self.balance = bal          # Correctly assign balance
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount      # Correct subtraction
        print("Rs.", amount, "was debited")

    # credit method
    def credit(self, amount):
        self.balance += amount      # Correct addition
        print("Rs.", amount, "was credited")

# Create an Account object
acc1 = Account(10000, 12345)

# Check initial values
print("Initial Balance:", acc1.balance)
print("Account No:", acc1.account_no)

# Try debit and credit
acc1.debit(500)
acc1.credit(41000)

# Check final balance
print("Final Balance:", acc1.balance)
