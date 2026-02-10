# Student College System

class Student:

    college_name = "ABC College"   # Class Variable (shared)

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print()
        

s1 = Student("madan", 101)
s2 = Student("Rahul", 102)

print("Before Changing College:\n")
s1.display()
s2.display()

Student.change_college("XYZ College")

print("After Changing College:\n")
s1.display()
s2.display()

print("Result Check:")
print("madan:", Student.is_pass(75))
print("Rahul:", Student.is_pass(30))


