n=int(input("enter the number"))
arr=[]
def fun123(n,arr):
    UNQ=5
    count=0
    for i in arr:
        if i<UNQ:
            count+=1
        if count==UNQ:
            print("UNQ")
        else:
            print("NOT UNQ")
fun123(n,arr)