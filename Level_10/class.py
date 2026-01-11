class Employee:
    language= "Python"  # class attribute
    salary = 150000

c1 = Employee()
c1.name = "Shanaya" #Object attribute/instance attribute
print(c1.language, c1.salary, c1.name)

c2 = Employee()
c2.name = "Neha"  #Object attribute/instance attribute
print(c2.salary, c2.language, c2.name)
