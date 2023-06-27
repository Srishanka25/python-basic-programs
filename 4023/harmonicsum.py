n=int(input("enter the number"))
def h_s(n):
    if n==1:
        return 1
    else:
        return 1/n+h_s(n-1)
print(h_s(n))
    