# inheritance 
class Parent:
    family_name="syeds"

    def family(self):
        print("There are a 5 peoples in the family the family name is",self.family_name)

class Child(Parent):
    child_name="nazneen"

    def printChildDetails(self):
        print(self.child_name,"is the child and she belongs to ",self.family_name)


p1=Parent()
p1.family()

c1=Child()
c1.printChildDetails()
c1.family()