def rotate_list(a,k):
    n=len(a)
    reverse_list(a,0,k-1)
    reverse_list(a,k,n-1)
    reverse_list(a,0,n-1)
def reverse_list(a,start,end):
    while(start<end):
        temp=a[start]
        a[start]=a[end]
        a[end]=temp
        start+=1
        end-=1
def printList(a):
    for i in a:
        print(i,end=" ")
    print()
a=[1, 3, 4, 2, 5]
reverse_list(a,2,4)
printList(a)
        
