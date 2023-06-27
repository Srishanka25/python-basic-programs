x=int(input("Enter No. of lines:"))
for i in range(x):
    asci=97
    width=0
    while width!=i:
        print(' ',end='')
        width+=1
    for j in range(x,i,-1):
        print(chr(asci),end=" ")
        asci+=1
    print("\n")