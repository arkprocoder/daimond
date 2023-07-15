name=input("enter the student name :\n")
kannada=int(input("enter the kannada mark:\n"))
hindi=int(input("enter the hindi mark:\n"))
english=int(input("enter the english mark:\n"))
maths=int(input("enter the maths mark:\n"))
science=int(input("enter the science mark:\n"))
social=int(input("enter the social mark:\n"))

if(kannada<0 or kannada>100 or hindi<0 or hindi>100 or english<0 or english>100 or maths<0 or maths>100 or science<0 or science>100 or social>100 or social<0):
    print("Give marks between 0-100")

else:    
    print("All marks correctly entered")
    totalmarks=kannada+maths+hindi+english+social+social
    avgmarks=totalmarks/6
    print("Total Marks = ",totalmarks)
    print("Average Marks = ",avgmarks)