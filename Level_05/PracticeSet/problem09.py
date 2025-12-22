# Can you change the values inside a list which is contained in set S?

# s = {8, 7, 12, "Shanaya" , [3, 5]}
# s[0] = 5  # ERROR  sets are immutable/hashable and lists are mutable/unhashable
# print(s)


# hashable object is an object that has a hash value which doesn't change during its entire lifetime

st = {8, 7, 12, "Shanaya"}

st.add(6)
print(st)
  
# adding multiple ele 

st2 = {5, 9, "rohan"}  # can be any list, tuple or another set

st.update(st2)
print(st)

st3 = {5, 2, 33}
st |= st3   # must be a set
print(st)

