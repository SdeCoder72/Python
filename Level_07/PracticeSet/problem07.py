# Write a program to print the following star pattern 

#      *
#    * * *
#  * * * * *  for n = 3
n = int(input("Enter a Number: "))
a = 0
for i in range(1, n+1):
    print("  " * (n-i), end="" )
    print("* " * (i+a), end="")
    a += 1
    print("\n")

for i in range(1, n+1):
    print("  " * (n-i), end="" )
    print("* " * (2*i - 1), end="")
    a += 1
    print("")
    # print("\n")