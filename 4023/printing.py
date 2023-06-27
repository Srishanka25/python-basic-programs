n=int(input("Enter No. of lines:"))
asci=97
for i in range(n):
    for j in range(i+1):
        print(chr(asci),end=' ')
    print('\n')
    asci+=1