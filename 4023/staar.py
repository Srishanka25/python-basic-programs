n=int(input("Enter no.of lines:"))
for i in range(n):
    space=0
    for k in range(n,i,-1):
        while space!=i:
            print(" ",end='')
            space+=1
        print("*",end=" ")
    print("\n")