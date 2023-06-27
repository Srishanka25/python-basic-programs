x=int(input("enter number"))
z=x
a=0
while x>0:
    rem=x%10
    a=a+rem*rem*rem
    x=x//10
if(z==a):
    print("armstrong number")
else:
    print("not an armstrong number")
    