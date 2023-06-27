'''def reverse_list(a):
    start=0
    end=len(a)-1
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
reverse_list(a)
printList(a)'''
def reverse_list(a,start,end):
    start=0
    end=len(a)-1
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
