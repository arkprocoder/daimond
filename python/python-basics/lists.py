# list: "collection of same or different data types"
'''

mylist=["apples","managoes","grapes",1,2,3,4,5,True,5.245,[1,2,3,4]]
print(type(mylist))
print(mylist)
print(len(mylist))
print(mylist[2])
print(mylist[8])
print(mylist[10])
print(mylist[10][2])

'''

'''
mylist=["mobile","car","bike","laptop"]
print(mylist)
print(mylist[2])
# want to replace bike with train
mylist[2]="train"
print(mylist)
'''

# list is mutable(change the element)

'''inbuilts functions of the list'''

mynum=[1,3,2,4,6,8,9,10,23,20,14,15]
print(len(mynum))
# mynum.sort()
# print(mynum)
mynum.append(100)
print(mynum)
mynum.insert(5,200)
print(mynum)
mynum.pop()
mynum.pop()
print(mynum)
mynum.remove(10)
print(mynum)
# mynum.clear()
print(mynum.count(1)) # repeated elements can be there in the list

l2=mynum.copy()
print(l2)