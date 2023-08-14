# abstract : 
# Hiding the unneccessary information to the user like anees
# we cannot create the object from the abstract class directly.
# we use abc module to import abstraction i.e ABC
# if we want to create the abstract class we need to inherit ABC
# if we want to create the object from the abstarct class we cannot create it directly but we can inherit the abstract class into a normal class then apply the abstarction
#we can create the abstract methods into abstract class
# when we create the new class which abstract class is inherited then we need to create all the methods which is present in the abstarct class 

from abc import ABC,abstractmethod

class Relationship(ABC):

    @abstractmethod
    def trust(self):
        pass

    @abstractmethod
    def care(self):
        pass

    @abstractmethod
    def fights(self):
        pass

    def love(self):
        print("i love you  soooooooooooooooo much it will be constant")

class Love(Relationship):
  
    def trust(self):
        print("i trust you")

 
    def care(self):
        print("i care you")


    def fights(self):
        print("i will fight for you")

 

obj=Love()
obj.trust()
obj.care()
obj.fights()
obj.love()