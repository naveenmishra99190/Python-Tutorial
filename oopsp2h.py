"""
1. static method
2. class method (cls)
3. Intance method (self)
"""

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    # ab hm chahate hai ki student class ke liye ek aur attribute hona chahiye jisko hm percentage kahenge basically
    # hm percentage attribute create krna chahate hai  
        self.percentage =str((self.phy + self.chem + self.math) / 3) + "%"

    def calcPercentage(self):
        self.percentage =str((self.phy + self.chem + self.math) / 3) + "%"

        
        
stu1 = Student(98, 97, 99)
print(stu1.percentage)

'''stu1.phy = 86
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)'''


#it's better method is property decorator:- 


