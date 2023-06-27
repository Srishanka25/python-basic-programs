n=input("enter a string")
k=""
b=""
s=0
for i in range(len(n)):
    if((n[i]>=chr(97) and n[i]<=chr(122 )or n[i]>=chr(65) and n[i]<=chr(90))):
        k+=n[i]
    if(n[i]>='0' or n[i]<='9' and n[i]>='0' or n[i]<='-9'):
        s+=int(n[i])
        b+=b[i]
print(k)
print(s)

    