class Student:


 # yaha pr student ek class hai to student ke liye we can create a contructor
 # all classes have a function called __init__(), which is always executed when the object is being initiated 
 # or yani jaise hi aap class ko use krke ek nayi class banaoge automatically __init__() function call ho jayega.   
 #  __init__() always execute hoga there will be always constructor for us , agr constructor hme khud likhana ho to hm aise likh sakte hai.
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("karan", 97)
print(s1.name,s1.marks)

s2 = Student("arjun", 88)
print(s2.name,s2.marks)