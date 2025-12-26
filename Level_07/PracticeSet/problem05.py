# Write a program to find the sum of first n natural numbers using while loop

n = int(input("Enter a Number: "))
i = 1
sum = 0
while(i <= n):
    sum += i
    i += 1

print(sum)
sum2 = int((n * (n+1) )/ 2)
print(sum2)