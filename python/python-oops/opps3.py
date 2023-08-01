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

    def returnemployeeDetails(self):
        return f"Company is {self.companyname}\nEmployee Name is {self.name}\nEmployee age is {self.age}\nEmployee salary is {self.salary}\nEmployee role is {self.role}\nEmployee place is {self.place}\n"

        
emp1=Employee("Nazneen",23,50000,"Frontend Developer","Bangalore") #step-1 created the emp1 object and we passed the arguments to class Employee
emp1.employeeDetails()
emp2=Employee("Anees",25,30000,"Full stack dev","bangalore")
emp2.employeeDetails()

emp3=Employee("Shuaib",25,30000,"dev","banaglore")
shuaib=emp3.returnemployeeDetails()
print(shuaib)

'''Create Candidate class
a)create Constructor which takes 4 arguements
[candidateName,candidateEmail,candidateCourse,CourseDuration]
create a function to print the candidateName,candidateEmail,candidateCourse,CourseDuration
'''