n=int(input("enter the size of the queue"))
def enqueue():
    element=input("enter the element for queue")
    queue.append(element)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty,add the element")
    else:
        e=queue.pop()
        print(e,"removed")
        print(queue)
queue=[]
while True:
    print("select the operation 1.enqueue 2.dequeue 3.quit")
    choice=int(input())
    if choice==1:
        dequeue()
    elif choice==2:
        enqueue()
    elif choice==3:
        break
    else:
        print("enter the correct operation!")

    