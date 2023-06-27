def sorted_merge(a,b):
    an=len(a)
    bn=len(b)
    ai=bi=0
    ans=[]
    while(ai!=an or bi!=bn):
        if(ai==an):
            ans.append(b[bi])
            bi+=1
        elif(bi==bn):
            ans.append(a[ai])
            ai+=1
        else:
            if(a[ai]<b[bi]):
                ans.append(a[ai])
                ai+=1
            else:
                ans.append(b[bi])
                bi+=1
    return ans

print(sorted_merge([1,2,3,5],[2,4,5,7]))
