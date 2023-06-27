y=int(input("enter the number:"))
if(y<0 and y>99999):
    print("invalid year")
elif(y%4==0  and (y%400==0 or y%100!=0)):
    print("leap year")
else:
    print("not a leap year")