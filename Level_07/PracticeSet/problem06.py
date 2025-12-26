# Write a program to calculate the factorial of a given number using for loop

n = int(input("Enter a Number: "))
i = 2
fact = 1
while(i <= n):
    fact *= i
    i += 1

print(f"factorial of {n} is: {fact}")