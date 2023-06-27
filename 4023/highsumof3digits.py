def max_sum_3(a):
    n=len(a)
    temp_sum = max_sum=0
    for s in range(0,n-2):
        temp_sum=sum(a[s:s+3])
        if(temp_sum > max_sum):
            max_sum = temp_sum
    return max_sum
#print(max_sum_k([3,5,15,20,2],5))
print(max_sum_3([3,5,15,20,2]))