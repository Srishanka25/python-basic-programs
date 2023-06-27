x=int(input("enter the number"))
y=int(input("enter the number"))
def lcm(x,y):
    z=x%y
    if(z==0):
        return x
    return x*lcm(y,z)/z
print(lcm(x,y))
        
        
        
        