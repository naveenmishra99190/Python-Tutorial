#write a recursive function to calculate the first natural numbers.
def calc_sum(n):
    if n == 0:
        return
    calc_sum(n-1)  # recursive call first
    print(n)        # print after recursion to get 1 → n

# Start the function
calc_sum(5)

