# def salary(sal):
#     print("Your salary is",sal)
#     salary=sal+5000
#     return salary

# anees=salary(15000)
# naz=salary(25000)
# dad=salary(35000)

# print("anees salary is ",anees)
# print("naz salary is ",naz)
# print("dad salary is ",dad)

def circle(r):
    res=3.14*r*r
    return res


def square(a):
    res=a*a
    return res


def rectangle(l,b):
    res=l*b
    return res


c=circle(5)
s=square(5)
r=rectangle(10,20)

print("area of the cicle is ",c)
print("area of the square is ",s)
print("area of the rectangle is ",r)
print("total",c+s+r)