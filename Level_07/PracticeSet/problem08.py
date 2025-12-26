# Write a program to print the following star pattern 

#   *
#   * *
#   * * *  for n = 3
n = int(input("Enter a Number: "))

for i in range(1, n+1):
    print("* "*i, end="")
    print()


# Java me aise hi hota h....
for i in range(1, n+1):
    for j in range(0, i):
        print("* ", end="")
    print()