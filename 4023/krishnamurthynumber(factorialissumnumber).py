def factorial(n):
    temp=n
    ans=1
    while(temp>0):
        ans*=temp
        temp-=1
    return ans
print(factorial(n))

def is_kn(n):
    temp=n
    sum=0
    while(temp>0):
        rem=temp%10
        temp//=10
        sum+=factorial(rem)
    if(sum==n):
        return True
    return False
n=int(input())
print(is_kn(n))