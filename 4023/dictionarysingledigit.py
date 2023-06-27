a=[3,0,0,8,0,3]
d={ }
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d.keys():
    if(d[i]==1):
        print(i)
        
    
