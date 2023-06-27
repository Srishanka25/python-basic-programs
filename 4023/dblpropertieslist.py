def insert_begin(self,data):
    new_node=Node(data)
    temp=self.head
    temp.prev=new_node
    new_node.next=temp
    self.head=new_node
def insert_end(self,data):
    new_node=Node(data)
    temp=self.head
    while temp.next is not None:
        temp=temp.next
    temp.next=new_node
    new_node.prev=temp
def insert_position(self,position,data):
    new_node=Node(data)
    temp=self.head
    for i in range(i,pos-1):
        temp=temp.next
    new_node.previous=temp
    new_node.next=temp.next
    temp.next.prev=new_node
    temp.next=new_node 
    
    
        
        