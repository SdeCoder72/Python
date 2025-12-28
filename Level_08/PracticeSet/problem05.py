# Write a program using functions to print first n lines of the following pattern:

'''
***
**
*   n = 3
'''


def pattern(n):
    for i in range(1, n+1):
        print("* "*(n-i-1), end="")
        print()

n = int(input("Enter number: "))
pattern(n)

# recusive function

def pattern2(n):
    if(n == 0):
        return
    print("* " * n)
    pattern2(n-1)

pattern2(n)
    