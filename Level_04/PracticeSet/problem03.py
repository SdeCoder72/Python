# Check that tuple type cannot be changed in python.

a = (4, 76, 2) # ERROR

a[2] = 43
print(a)