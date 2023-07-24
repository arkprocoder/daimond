# string positive slicing
mystr="my name is doremon"
print(mystr[0:5]) #my nam [start:end-1]
print(mystr[11:19])
print(mystr[8:])
print(mystr[:])
print(mystr[:9])

print(mystr[0:19:2])  #[start:end-1:sep-1]
print(mystr[::6])
print(mystr[2:10:3]) # ' mi'
print("\n")
print("string negative slicing")
# my name is dore     m     o     n
# -18                 -3,  -2,   -1
mystr="my name is doremon"
print(mystr[-1])
print(mystr[-2])
print(mystr[-3])

print(mystr[-10:-1]) #[start:end-1] 
print(mystr[-14:])
print(mystr[::-1]) # this is use to reverse the string
print(mystr[::-2])