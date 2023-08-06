# single level inheritance with constructor
class Parent:
    haircolor="Black"
    def __init__(self,name,height,bloodgroup,weight):
        self.fullname=name
        self.height=height
        self.blood=bloodgroup
        self.weight=weight
        print("Parent constructor is ran")

    def ParentDetails(self):
        print(f"\nName is {self.fullname}\nHeight is {self.height}\nBlood group is {self.blood}\nWeight is {self.weight}\nHair Color is {self.haircolor}")

class Child(Parent):
    
    def __init__(self,name,height,bloodgroup,weight,age):
        self.fullname=name
        self.height=height
        self.blood=bloodgroup
        self.weight=weight
        self.age=age
        print("Child constructor is ran")

    def ChildDetails(self):
        print(f"\nName is {self.fullname}\nHeight is {self.height}\nBlood group is {self.blood}\nWeight is {self.weight}\nHair Color is {self.haircolor}\nAge is {self.age}")


c1=Child("ark","6.0","B+",98)
c1.ChildDetails()
c1.ParentDetails()

p1=Parent("z",3,"o",87)
p1.ParentDetails()