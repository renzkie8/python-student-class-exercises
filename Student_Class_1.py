class Student:
    def __init__(self, name, age, address, year, section, program):
        self.name = name
        self.age = age
        self.address = address
        self.year = year
        self.section = section
        self.program = program

    def input(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nYear/Level: {self.year}\nSection: {self.section}\nProgram: {self.program}")

name = input("Enter Student's Name: ")
age = input("Enter Student's Age: ")
address = input("Enter Student's Address: ")
year = input("Enter Student's Year/Level: ")
section = input("Enter Student's Section:")
program = input("Enter Student’s Program:")

student1 = Student(name, age, address, year, section, program)
student1.input()
