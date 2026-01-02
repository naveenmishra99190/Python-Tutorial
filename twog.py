a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a == b == c:
    print("All values are equal")
elif (a >= b) and (a >= c):
    print("a is greatest")
elif (b >= a) and (b >= c):
    print("b is greatest")
else:
    print("c is greatest")
