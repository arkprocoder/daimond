# args:arguements

'''
def naz(*args):
    print(type(args))
    print(args) #(["good",5.2,"4xl","black","85kg"],)
    for i in args:
        # print(1)
        print(i) # ["good",5.2,"4xl","black","85kg"]
        print(type(i)) #list


args=["good",5.2,"4xl","black","85kg"]
naz(args)
'''

# **kwargs :keyword arguements

'''
def kwargFunc(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(type(kwargs.items()))
    for key,value in kwargs.items():
        print(key, value)
        print(type(key),type(value))

mydict={
    "employeeName":"Rohan",  #key:value
    "employeeSalary":15000.52,
    "isActive":True,
    "role":"Front end dev",
    "address":['bangalore','devenhalli'],
    "phoneNumber":9874563210,
    "hobbies":("dance","sing"),
    "skills":{"python","django"},  
}

kwargFunc(**mydict)

'''
'''
def args_kwarg(*args, **kwargs):

    print(type(args))
    print(args) #(["good",5.2,"4xl","black","85kg"],)
    for i in args:
        # print(1)
        print(i) # ["good",5.2,"4xl","black","85kg"]
        # print(type(i)) #list

    print(kwargs)
    print(type(kwargs))
    print(type(kwargs.items()))
    for key,value in kwargs.items():
        print(key, value)
        # print(type(key),type(value))


args=["good",5.2,"4xl","black","85kg"]

kwargs={
    "employeeName":"Rohan",  #key:value
    "employeeSalary":15000.52,
    "isActive":True,
    "role":"Front end dev",
    "address":['bangalore','devenhalli'],
    "phoneNumber":9874563210,
    "hobbies":("dance","sing"),
    "skills":{"python","django"},  
}
args_kwarg(args,**kwargs)

'''

def args_kwarg(name,*args, **kwargs):
    print(name)
    print(type(args))
    print(args) #(["good",5.2,"4xl","black","85kg"],)
    for i in args:
        # print(1)
        print(i) # ["good",5.2,"4xl","black","85kg"]
        # print(type(i)) #list

    print(kwargs)
    print(type(kwargs))
    print(type(kwargs.items()))
    for key,value in kwargs.items():
        print(key, value)
        # print(type(key),type(value))


args=["good",5.2,"4xl","black","85kg"]

kwargs={
    "employeeName":"Rohan",  #key:value
    "employeeSalary":15000.52,
    "isActive":True,
    "role":"Front end dev",
    "address":['bangalore','devenhalli'],
    "phoneNumber":9874563210,
    "hobbies":("dance","sing"),
    "skills":{"python","django"},  
}
name="Nazneen Anjum"
args_kwarg(name,args,**kwargs)
