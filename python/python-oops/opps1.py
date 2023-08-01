class Person:
    name="Human Name" #data members of the class
    age="Human Age"
    height="Human Height"

    def eat(self):#self is object address
        print("Human Eats")

    def sleep(self):
        print("Human sleeps")

    def laugh(self):
        print("Hman laugh")

    def returnAge(self):
        return 25

obj=Person() #we creates a object as instance from Person class i.e Blueprint
print(obj.name) #we are accessing the data member from the class
print(obj.age)
print(obj.height)
obj.eat()

person1=Person()
person2=Person()
person3=Person()
person4=Person()
person5=Person()

person3.laugh()
print(person3.returnAge())
print(person5.name)
print(person4.name)