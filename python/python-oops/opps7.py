#multiple inheritance without constructor

class A():
    name="Class A"
    def Adetails(self):
        print("i m the A details")

class B(A):
    name="Class B"
    def Bdetails(self):
        print("i m the B details")

class C(B):
    name="Class C"
    def Cdetails(self):
        print("i m the C details")

class D(C):
    name="Class D"
    def Ddetails(self):
        print("i m the D details")


d=D()
d.Ddetails()
d.Cdetails()
d.Bdetails()
d.Adetails()
print(d.name)