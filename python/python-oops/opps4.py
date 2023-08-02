class Employee:
    companyname="Infosys"
#step-2 :constructor will get called automatically whenever we create the objects and it will initialize the data members of the class
    def __init__(self,name,age,salary,role,place): #constructor
        self.name=name
        self.age=age
        self.salary=salary
        self.role=role
        self.place=place
        # print("my constructor is running")

    def employeeDetails(self):
        print(f"Company is {self.companyname}\nEmployee Name is {self.name}\nEmployee age is {self.age}\nEmployee salary is {self.salary}\nEmployee role is {self.role}\nEmployee place is {self.place}\n")


    @staticmethod
    def publicHoliday(name):
        print(name,"August 15 is public holiday")

    @classmethod
    def changeCompany(self,cls):
        self.companyname=cls
        print("Your Company Name is ",self.companyname)


        
emp1=Employee("Nazneen",23,50000,"Frontend Developer","Bangalore") #step-1 created the emp1 object and we passed the arguments to class Employee
emp1.employeeDetails()
emp2=Employee("Anees",25,30000,"Full stack dev","bangalore")
emp2.employeeDetails()
emp1.publicHoliday("naz")
emp2.publicHoliday("anees")

emp1.changeCompany("TCS")
emp1.employeeDetails()


'''Create Candidate class
a)create Constructor which takes 4 arguements
[candidateName,candidateEmail,candidateCourse,CourseDuration]
create a function to print the candidateName,candidateEmail,candidateCourse,CourseDuration
'''