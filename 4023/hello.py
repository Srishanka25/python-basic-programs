n=(input("enter the string"))
str1=" "
str2=" "
for i in range(len(n)):
    if(n[i]>='0' or n[i]<='9'):
        str+=n[i]
    if(n[i]>=chr(97) or n[i]<=chr(122) and n[i]>=chr(65) or n[i]<=chr(90)):
        str+=n[i]
print(str1)
print(str2)
