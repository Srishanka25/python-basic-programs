k=int(input("enter the date"))
m=int(input("enter the month"))
y=int(input("enter the year"))
c=y//100
d=y%100
if((k>31 or k<0 or m>12 or k<0 or y>9999 or y<1000)):
    print("invalid")
if(y%4==0 or m==2):
    k<=29 
else:
    k<=31
if(m==1):
    m=13
elif(m==2):
    m=14
else
    m=m-1 
f=k+(13*m-1)/5+d+d/4+c/4-5*c
result=f%7
if(result==0):
    print("sunday")
elif(result==1):
    print("monday")
elif(result==2):
    print("tuesday")
elif(result==3):
    print("wednesday")
elif(result==4):
    print("thursday")
elif(result==5):
    print("friday")
else:
    print("saturday")

    
    




                                                                                                  