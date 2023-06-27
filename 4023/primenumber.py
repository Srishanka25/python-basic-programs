n=int(input("Enter a Number:"))
x=0
for i in range(2,n):
    if n%i==0:
        print(n,"is not a Prime Number")
        x=1
        break
if (x==0):
    print(n,"is a Prime Number")