mylist=["tomato","onion","potato","chilli","carrot","cucumber","rice"]
#       [0       ,   1   ,   2     ,   3,       4    ,    5    ,   6]
#       [-7       ,  -6   ,  -5     ,  -4,      -3    ,    -2    ,   -1]
print(mylist[:]) #[start:end]
print(mylist[1:5]) #[start: end-1]
print(mylist[5:1]) #[start: end-1] #empty becuz its looks always to left to right and make sure your start should me smaller than end

print(mylist[::2]) #[start: end-1 : seprator-1]
print(mylist[::6]) #[start: end-1 : seprator-1]

print("negative slicing")

print(mylist[-5])
print(mylist[-5:])
print(mylist[-5:-1]) #[start: end-1]
print(mylist[-2:-5]) #-2 is more -5 is less so start is > end
print(mylist[-5:-2]) #-2 is more -5 is less so start is > end

# note: Always start should be less than end
print(mylist[::-1])
print(mylist[::-2])