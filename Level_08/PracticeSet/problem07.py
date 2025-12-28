# # Write a program using functions to remove a given word from a list add strip it at the same time.

l = ["Shanaya", "Anaya","Sharansh", "Kavya", "ansh"]

def rem(l, word):
    n = []
    for i in l:
        if not(i == word):
            n.append(i.strip(word))
    return n

print(rem(l, "ansh"))

