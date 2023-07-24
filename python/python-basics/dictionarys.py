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
print(mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.items())

mydict.update({
    "employeeSalary":252502.25,
    "isExperienced":False
})

print(mydict)
print(mydict.get("phoneNumber"))
print(mydict.get("employeeSalary"))
# print(mydict.get("anees"))
# mydict.clear()
# mydict2=mydict.copy()
mydict.pop("isExperienced")
print(mydict)

mydict.popitem()
print(mydict)