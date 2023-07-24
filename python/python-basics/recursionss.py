# write a program to find the factorial of any number

# 5!
# 5*4*3*2*1

# algorithm
'''
factorial(n)= n*factorial(n-1)
factorial(5)= 5*factorial(5-1)
factorial(5)= 5*factorial(4)
factorial(4)= 5*4*factorial(4-1)
factorial(4)= 5*4*factorial(3)
factorial(3)= 5*4*3*factorial(3-1)
factorial(3)= 5*4*3*factorial(2)
factorial(3)= 5*4*3*2*factorial(2-1)
factorial(2)= 5*4*3*2*factorial(1)

if factorial(1)=1 or factoraial(0)=1
factorial(1)= 5*4*3*2*1
factorial(5)= 120
'''

print(23)
num=int(input("Enter the number to find the factorial \n"))
def factorial(n):
    print(26)
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
print(30)
res=factorial(num)
print(32)
print(f"factorial of {num} is {res}")
print(34)



'''
# tracing
# num=5
#1
def factorial(5):
    # if n==1 or n==0:
    #     return 1
    return 5*factorial(5-1)
    return 5*factorial(4)

def factorial(4):
    # if n==1 or n==0:
    #     return 1
    return n*factorial(n-1)
    return 5*4*factorial(3)

def factorial(3):
    # if n==1 or n==0:
    #     return 1
    return n*factorial(n-1)
    return 5*4*3*factorial(2)

def factorial(2):
    # if n==1 or n==0:
    #     return 1
    return n*factorial(n-1)
    return 5*4*3*2*factorial(1)

def factorial(1):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
    return 5*4*3*2*1

# 120
'''