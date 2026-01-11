class Employee:
    language= "Python"  
    salary = 150000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("This is a dunder method which is called automatically as soon as object is created.")
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")

c1 = Employee("Harry", 1600000, "JS")
c1.name = "Shanaya" 
print(c1.language, c1.salary, c1.name)