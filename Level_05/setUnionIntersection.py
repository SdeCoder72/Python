s1 = {2, 5, 7, 4, 23}
s2 = {4,7, 23, 76,4}
print(s1.union(s2))
print(s1.intersection(s2)) # repeated valua 

print(s1.difference(s2))

print({2, 5}.issubset(s1))
print({2, 6}.issubset(s1))
print(s2.issuperset(s1))

s2.clear()
print(s2)

print(s1.pop())
print(s1)