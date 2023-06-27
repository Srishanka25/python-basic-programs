def max_sum(a,k):

def max_sum_k(a,k):
    
        n=len(a)
        temp_sum = max_sum=sum(a:[:k])
        s=1
        e=k
        while(e<n):
            print(temp_sum,a[s-1],a[e])
            temp_sum-=a[s-1]
            temp_sum+=a[e]
            
        if(temp_sum > max_sum):
            max_sum = temp_sum
            s+=1
            e+=1
        for s in range(0,n-2):
            if(temp_sum > max_sum):
                max_sum=temp_sum
    return max_sum
print(max_sum_k([3,5,15,20,2],5))
print(max_sum([3,5,15,20,2],5))