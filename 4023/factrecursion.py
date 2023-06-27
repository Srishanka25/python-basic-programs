def factorial(n):
    temp=n
    ans=1
    while(temp>0):
        ans*=temp
        temp-=1
    return ans
n=int(input())
print(factorial(n))