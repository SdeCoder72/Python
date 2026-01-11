# Create a class with a class attribute a; create an object from it and set "a" directly using object.a =0. Does this change the class attribute

class cls:
    a = 8

obj = cls()
print(obj.a)
obj.a = 0  # overwrite 8 to 0 by instance attribute
print(obj.a)
print(cls.a)  # but it'll not affect class attribute
