# method overloading & over riding
class A():
    def __init__(self,lpname,lpmodel,lpprice):
        self.lpname=lpname
        self.lpmodel=lpmodel
        self.lpprice=lpprice

    def laptop(self):
        print(self.lpname,self.lpmodel,self.lpprice)

class B(A):
    def __init__(self,lpname,lpmodel,lpprice,genration):
        super().__init__(lpname,lpmodel,lpprice)
        self.genration=genration

    def laptop(self):
        print(self.lpname,self.lpmodel,self.lpprice,self.genration)


l1=B("lenevo",2021,50000,"i7")
l1.laptop()