# sets
# s1={1,2,3,4,5,6,7,8,2,34,5,6,7,90,10,34,22,26}
# print(type(s1))
# print(s1)
# print(s1[3])

s=set()
print(s)
print(type(s))
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)

s2={1,2,3,6,7,8,9,10}
print(s.union(s2))
print(s.intersection(s2))
print(len(s2))
s2.remove(8)
print(s2)
s2.clear()
print(s2)


s3={10,11,12,1,2,3,4,9,8,7,6,5}
s4=s3.copy()
print(s3)
print(s4)

s6={12,1,2,3,4,9,8,"anees","naz",True,[1,2,3]}
print(s6)