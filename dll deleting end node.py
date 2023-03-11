class Node:
    def __init__(self,data):
        
        self.data=data
        self.previous=None
        self.next=None
class DLL:
    
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next         #first move the pointers and at lest make the segments null
            prev=prev.next
        prev.next=None
        temp.prev=None
       
    def display(self):
        if self.head is None :
            print("DLL is empty")
        else :
            temp=self.head
        while(temp):
            print(temp.data,"<==>",end=" ")
            temp=temp.next
obj=DLL()
n1=Node(100)
obj.head=n1 
n2=Node(200)
n2.previous=n1
n1.next=n2
n3=Node(300)
n3.previous=n2
n2.next=n3
n4=Node(400)
n4.previous=n3
n3.next=n4
print("before deletion")
obj.display()
obj.delete_end()
print("")
print("after deletion ")
obj.display()

