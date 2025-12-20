a = 'Shanaya'
b = "Anaya"
c = '''John'''

# Strings are immutable

name = "Kavya"

#slicing the string
shortName = name[1:4]   # slicing 1 to 4 - 1 in inclusive and 4 is exclusive

print(shortName)

# character from string
char = name[3]
print(char)

# -ve slicing
name2 = "Shanaya"
print(name2[-6: -1])
print(name2[1: 6])
print(name2[:4]) # smae as print(name2[0:4])
print(name2[3:]) # same as print(name2[3:len(name2)])

word = "amazingly"
print(word[1:7:3])