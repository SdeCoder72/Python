class Employee:
    language= "Python"  # class attribute
    salary = 150000
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def greet(self):
        print(f"Good morning {self.name}")

    @staticmethod
    def greet2():
        print("Good morning ") 



c1 = Employee()
c1.name = "Shanaya" #Object attribute/instance attribute
print(c1.language, c1.salary, c1.name)

c1.getInfo()
Employee.getInfo(c1)  # same as above

c1.greet()
Employee.greet(c1)
c1.greet2()
