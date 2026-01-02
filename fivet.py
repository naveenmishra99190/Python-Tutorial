# WAP to find the factorial of first n numbers (using for)

n = 5 
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print("factorial = ", fact)    


'''
e ek while loop hai jo tab tak chalega jab tak i ≤ n hai.
fact *= i ka matlab hai fact = fact * i
Pehli baar: 1 × 1 = 1
Doosri baar: 1 × 2 = 2
Teesri baar: 2 × 3 = 6
Chauthi baar: 6 × 4 = 24
Paanchvi baar: 24 × 5 = 120
i += 1 se har baar i me 1 badh jaata hai, taaki loop agle number pe jaaye.
'''