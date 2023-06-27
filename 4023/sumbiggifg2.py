l=list(map(int,input().split()))
curr_max=l[0]
res=l[0]
for i in range(1,len(l)):
    if l[i]>curr_max:
        curr_max=l[i]
        res+=curr_max
print(res)