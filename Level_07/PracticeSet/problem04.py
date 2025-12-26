# Write a program to find whether a given number is prime or not
n = int(input("Enter a Number: "))
limit = int(n/2+1)
for i in range(2, limit):
    if(n%i == 0):
        print("Not a prime Number")
        break
else:
    print("Prime number")