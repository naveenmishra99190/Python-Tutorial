f = open("demo.txt", "r")


data = f.read()
print(data)

# because of above read data below line will not print

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

