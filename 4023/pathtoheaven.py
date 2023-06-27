n=int(input())
def PTH(n):
    count=0
    if n%3==0:
        n=n/3
        count+=1
    elif n%2==0:
        n=n/2
        count+=1
    else:
        n=n-1
        count+=1
print(count)
PTH(n)

        