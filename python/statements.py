'''
# condition statements
1. if
2. if -else
3. elif ladder

'''
# age=int(input("enter your age:\n"))
# if(age<18):
#     print("You cannot vote")
# else:
#     print("You Can Vote")

'''
# java
if(age<18){
print("You cannot vote")
print("i am in if")
}

else{
    print("i am in else")
print("You Can Vote")
}
'''
'''
age=int(input("enter your age:\n"))
if(age<18):
    print("inside if statement")
    print("You cannot vote")
    print("you are not matured")
    print("you are not eligible")
else:
    print("inside else statement")
    print("You Can Vote")
    print("You are MAtured")
    print("You are eligible")

print("i am outside if else statement")
print("i am python program")
'''


# age=int(input("enter your age:\n"))
# if(age<18):
#     print("inside if statement")
#     print("You cannot vote")

# elif(age>18 and age<=70):
#     print("You can vote")

# elif(age>70 or age<=100):
#     print("Enjoy your last days")
    
# else:
    # print("i am else")


age=int(input("enter your age:\n"))
if(age<18):
    print("inside if statement")
    print("You cannot vote")

elif(age>18):
    print("You can vote")

elif(age<70):
    print("Enjoy your last days")

else:
    print("You cannot vote")