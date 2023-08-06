class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def StudentDetails(self):
        print(f"Student name is {self.name}\nStudent Age is {self.age}")


class Teacher:
    def __init__(self,name,age,role,salary):
        self.name=name
        self.age=age
        self.role=role
        self.salary=salary

    def TeacherDetails(self):
        print(f"Teacher name is {self.name}\nTeacher Age is {self.age}\nRole is {self.role}\nSalary is {self.salary}")


class School(Teacher,Student):
    def __init__(self,name,age,role,salary,schoolname):
        self.name=name
        self.age=age
        self.role=role
        self.salary=salary
        self.schoolname=schoolname

    def Details(self):
        print(f"Teacher name is {self.name}\nTeacher Age is {self.age}\nRole is {self.role}\nSalary is {self.salary}\nScholl name {self.schoolname}")



obj1=School("umesh",35,"maths teacher",20000,"ruby")

obj1.Details()
obj1.TeacherDetails()
obj1.StudentDetails()