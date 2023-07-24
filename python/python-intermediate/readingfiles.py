# f=open("data.txt")
# content=f.read()
# print(content)
# f.close()

# f=open("data.txt","rt")
# content=f.read(10)
# print(content)
# f.close()

# f=open("data.txt")
# content=f.readline()
# print(content)
# content=f.readline()
# print(content)
# content=f.readline()
# print(content)
# f.close()


# f=open("data.txt","rt")
# content=f.readlines()
# print(content[29:36])
# f.close()

with open("data.txt") as content:
    data=content.read()
    print(type(data))
    print()

    