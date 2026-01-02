#Multiple Inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "welcometo class B" 

class C(A, B):  # dono class A, B ki property inherit karegi
    varC = "welcome to class C"      

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)