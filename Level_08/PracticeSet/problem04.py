# Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter number: "))

def naturalNum(n):
    if(n == 1):
        return 1
    return n + naturalNum(n-1)

print(naturalNum(n))