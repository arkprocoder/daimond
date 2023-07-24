mystr="my name is doremon"
print(mystr)
print(len(mystr))
print(mystr.upper())
print(mystr.lower())
# print(mystr)
# mystr=mystr.upper() # = : assignment operator
# print("original str is ",mystr)
print(mystr.capitalize())
print(mystr.endswith("mon"))
print(mystr.endswith("naz"))
print(mystr.endswith(" doremon"))
print(mystr.startswith("my"))
print(mystr.startswith("My"))
print(mystr.count("n"))
print(mystr.count("z"))
print(mystr.count("name"))
print(mystr.count(" "))
print(mystr.find("my"))
print(mystr.find("n"))

'''
my name is doremon
012345678910

'''
print(mystr.find("z"))
print(mystr.isalnum())
print(mystr.isdigit())
name="ark"
print(name.isalpha())
print(mystr.isprintable())