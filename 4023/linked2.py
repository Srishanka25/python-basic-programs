class Node:
    def init(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,'->',end=" ")
    
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                temp=temp.next
                
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=None
obj.display()