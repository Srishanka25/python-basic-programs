def is_palindrome(a, s, e):#a is the string to check,s is starting index,ending index
    if(s>=e):
        return True
    if(a[s]!=a[e]):
        return False
    return is_palindrome(a,s+1,e-1)
a="STSTST"
print(is_palindrome(a,0,len(a)-1))
    
     
        
    
    
    