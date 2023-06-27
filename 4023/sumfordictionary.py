a=[0,-5,-3,4,15]
x=-8
c=0
for i in range(0,len(a),1):
    for j in range(1,len(a),1):
        k=a[i]+a[j]
        if(k==x):
            print("(",a[i],",",a[j],")")
            c=c+1
if(c>=0):
    print("true")
else:
    print("no")
d={}
for i in range(len(a)):
    for i in d:
        d[i]=a[i]
        if(a[i]+d[i]==x):
            print("yes")
        else:
            print("no")
        