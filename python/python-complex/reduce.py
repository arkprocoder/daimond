from functools import reduce

x=[1,2,3,4,5]
# x=[2,3,4,5]
# x=[6,4,5]
# x=[24,5]
# x=[120]

res=reduce((lambda x,y:x*y),x)
print(res)
print(type(res))