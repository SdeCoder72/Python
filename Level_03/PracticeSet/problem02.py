# Write a program to fill in a letter template given below with name and date

# letter = '''
#     Dear <|Name|>,
#     You are selected
#     <|Date|>
# '''


name = input("Enter your Name: ")
date = input("Enter date: ")
letter = '''
    Dear <|Name|>,
     You are selected
    <|Date|>
    '''
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))

