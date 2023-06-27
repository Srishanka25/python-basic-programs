a=[1,0,1,0,8,0,1]
for i in range(0,len(a),1):
    count=0
    for j in range(0,len(a),1):
        if(a[i]==a[j]):
            count=count+1
    if(count==1):
        print(a[i])
