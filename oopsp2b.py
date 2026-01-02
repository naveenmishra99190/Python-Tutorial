# private attributes & method : sensitive information are within the class not accessible from outside the class.
# isko private banane ke liye uske aage do underscore laga dete hai.

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        # above two underscore

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.__acc_pass)
