'''def symmetrical(a):
    n=len(a)
    s1=0
    s2=n//2
    while(s2<n):
        if(a[s1]!=a[s2]):
            return False
        s1+=1
        s2+=1
    return True
print(symmetrical("wow"))
print(symmetrical("abab"))
print(symmetrical("cadcad"))'''

def is_symmetric(a, s1, s2):#a is the string to check,s is starting index,ending index
    if(s2>=len(a)):
        return True
    if(a[s1]!=a[s2]):
        return False
    return is_symmetric(a,s1+1,s2)
def sym(a):
    return is_symmetric(a,0,len(a)//2)
print(sym("ABBAABBA"))
    
    