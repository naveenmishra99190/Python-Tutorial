# WAP to find the sum of first seven natural numbers Use WHILE loop.
# sum = 1+2+3+4+5
n = 7
sum = 0
i = 0  # Initialize i before using it

while i <= n:
    sum += i
    i += 1

print("total sum =", sum)




# WAP to find the sum of first Five natural numbers Use for loop.
# sum = 1+2+3+4+5
n = 5
sum = 0
for i in range(1,n+1):
    sum += i
print("total sum =",sum)    
