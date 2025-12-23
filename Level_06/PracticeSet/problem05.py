# Write a program which finds out whether a given name is present in a list or not.
l = ["Shanaya", "Anaya", "Avi", "Pratham", "Neha"]

name = input("Enter name: ")

if(name in l) :
    print(f"{name} is present in the list")
else:
    print(f"{name} is not present in the list")