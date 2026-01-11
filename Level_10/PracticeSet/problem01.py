# Create a Class "Programmer" for storing info of few programmers working at Microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p1 = Programmer("Shanaya", 1500000, 214375)
print(p1.name, p1.salary, p1.pin)