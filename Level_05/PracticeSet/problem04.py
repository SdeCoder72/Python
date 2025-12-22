# What will be the lengt of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add(20.00)
s.add("20") 

# 2
print(s)
print(len(s))
f = type(20.0)
i = type(20)
print(f == i)
print(20 == 20.0)