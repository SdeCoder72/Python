# If the names of 2 friends are same; What will happen to the program in problem 6
d = {}

name = input("Enter friend's name: ")
lang = input("Enter the Coding Language: ")
d.update({name : lang})

name = input("Enter friend's name: ")
lang = input("Enter the Coding Language: ")
d.update({name : lang})

name = input("Enter friend's name: ")
lang = input("Enter the Coding Language: ")
d.update({name : lang})

name = input("Enter friend's name: ")
lang = input("Enter the Coding Language: ")
d.update({name : lang})

name = input("Enter friend's name: ")
lang = input("Enter the Coding Language: ")
d.update({name : lang})
print(d)


# Enter friend's name: shubam
# Enter the Coding Language: python
# Enter friend's name: rohan
# Enter the Coding Language: python
# Enter friend's name: ravi
# Enter the Coding Language: c++
# Enter friend's name: ravi
# Enter the Coding Language: java
# Enter friend's name: sam
# Enter the Coding Language: ruby
# {'shubam': 'python', 'rohan': 'python', 'ravi': 'java', 'sam': 'ruby'}

# Answer
# it'll update the name's value and not create anothe key-value