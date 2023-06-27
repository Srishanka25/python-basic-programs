def equilateral_triangle(n):
    m=n-1
    for i in range(0,n):
        for j in range(0,m):
            print(" ",end=" ")
    m=m-1
    for j in range(0,i+1):
        print("*",end=" ")
    print()
    n=int(input())
    right_triangle(n)

