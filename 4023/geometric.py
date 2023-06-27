n=int(input("enter the number"))
def g_s(n):
    if(n==1):
        return 1
    else:
        return (1/pow(2,n))+g_s(n-1)
print(g_s(n))