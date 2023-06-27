n=int(input())
list=[]
for i in range(1,n//2):
    if(n%i==0):
        list.append(i)
print(list)