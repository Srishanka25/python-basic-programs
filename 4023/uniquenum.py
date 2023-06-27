a=[1,2,4,4,2,10]
n=int(input("enter the number"))
count=0
for i in range(0,len(a)):
    if(a[i]<n):
        count=count+1
if(count==n):
    print("unique number")
else:
    print("not a unique number")
        
        