class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
Node1=Node("Srishanka")
SL=SLL
SL.head=Node1
Node2=Node("Srija")
SL.head=Node2
Node3=Node("Harshini")
SL.head=Node3
Node4=Node("Varshini")
print(Node4.next)
print(Node2.next)