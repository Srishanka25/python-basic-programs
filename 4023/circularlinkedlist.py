class Node:
    def __init__(self,data):
        self.data=data
        self.tail=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def display(self):
        if self.head is None:
            print("empty circular link list, add some elements")
        else:
            temp=self.head
            while temp!=self.head:
                temp=temp.next
                print(temp.data)
            print(temp.next.data)
    def insert_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node=self.head
            self.head=new_node
            self.tail.next=self.head
'''cl.insert_beginning(40)
cl.display()'''
     #def insert_end(self,data):
      def insert_pos(self,pos,data):
          new_node=Node(data)
          if self.head is None:
              self.head=new_node
              self.tail=new_node
              self.tail.next=self.head
          else:
              if pos==1:
                  insert_beginning(data)
              else:
                  temp=self.head
                  for i in range(1,pos-1):
                      temp=temp.next
                  new_node.next=temp.next
                  temp.next=newnode
      def delete_pos(self,pos):
          if self.head is None:
              print("CLL is Empty")
          elif pos==1:
              delete_end()
          else:
              temp=self.head.next
              prev=self.head
              for i in range(1,pos-1):
                  temp=temp.next
                  prev=prev.next
              prev.next=temp.next
              
                  
           
         
              
            
                 
                
node_1=Node(10)
node_2=Node(20)
node_3=Node(30)
print(node_1)
print(node_2)
print(node_3)
cl=cll()
cl.head = node_1
cl.tail= node_1
cl.tail.next=cl.head
print(cl.head.next)
node_1.next=node_2
cl.tail=node_2
cl.tail.next=cl.head
print(node_1.next)
print(cl.tail.next)
print(node_2.next)
node_2.next=node_3
cl.tail=node_3
cl.tail.next=cl.head
cl.display()
cl.insert_beginning(40)
cl.display()

            





        