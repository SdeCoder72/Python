# Write a program to print multiplication table of n using for loop in reversed order. 

n = int(input("Enter a Number: "))
i = 10
while(i > 0):
    print(f"{n} X {i} = {n*i}")
    i -= 1


for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")