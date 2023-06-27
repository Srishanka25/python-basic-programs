number=int(input("Enter No. of lines:"))
for i in range(number):
    asci=97
    space=0
    while space!=i:
        print(' ',end='')
        space+=1
    for j in range(number,i,-1):
        print(chr(asci),end=" ")
        asci+=1
    print("\n")