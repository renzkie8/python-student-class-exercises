class Student:
    def __init__(self):
        self.name = self.get_valid_name()
        self.age = self.get_valid_age()

    def get_valid_name(self):
        while True:
            name = input("Enter student's name: ")
            if name.replace(" ", "").isalpha():
                return name
            print("Please enter a valid name with only letters in the alphabet.")

    def get_valid_age(self):
        while True:
            try:
                age = int(input("Enter student's age: "))
                if age > 0:
                    return age
                print("Age should be a positive integer.")
            except ValueError:
                print("Please enter a positive integer for age.")

    def display(self):
        print(f"Student Information received:\nName: {self.name}\nAge: {self.age}")

# Creating an object of Student class and displaying the information
student = Student()
student.display()
