# multiple inheritance

class Employee1:
    def employee1():
        pass

class Employee2:
    def employee2():
        pass

class Company(Employee1,Employee2):
    def company():
        pass



c1=Company()


# Daimond Problem

class Employee1:
    def employee1():
        pass

class Employee2(Employee1):
    def employee2():
        pass

class Company(Employee2):
    def company():
        pass



c1=Company()
