 def border_num(n:int):
     x=1
     arr=[[" " for i in range:(0,n)] for i in range(0,n)]
     i=0
     j=0
     while(j<n):
         arr[i][j]=x
         j+=1
         x+=1
    i=n-1
    j=n-2
    while(j>=0):
        arr[i][j]=x
        j=-1
        x+=1
    pad=len(str(x))
    print_2d(arr,n,pad)
    
def print_2d(a,n,pad):
    for i in range(0,n):
        for j in range(0,n):
            if(isinstance(a[i][j],str):
               print(" ",pad,end=" ")
            else:
               print(("{0:"+str(pad)+")").format(a[i])
               print()

                     