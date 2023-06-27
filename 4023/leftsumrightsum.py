l=list(map(int,input().split()))
res=[]
for i in range(0,len(l)):
    ls=sum(l[:i])
    rs=sum(l[i+1:])
    res.append(abs(ls-rs))
print(res)
        
        
        
        