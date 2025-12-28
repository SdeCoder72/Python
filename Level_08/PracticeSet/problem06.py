# Write a python function which converts inches to cms.


def inch_to_cms(inch):
    return inch * 2.54

inches = int(input("Enter value in inches: "))

print(inch_to_cms(inches))