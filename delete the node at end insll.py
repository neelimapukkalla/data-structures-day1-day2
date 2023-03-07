#delete at end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head = None
    def delete(self):
            temp=self.head.next
            prev=self.head
            while temp.next is not None:
                temp=temp.next
                prev=prev.next
            prev.next=None
    def display(self):
            if self.head is None:
                print("ll is empty")
            else:
                temp=self.head
            while(temp):
                print(temp.data,"==>",end=" ")
                temp=temp.next
obj=sll()
n1=Node(200)
obj.head=n1
n2=Node(300)
obj.head.next=n2
n3=Node(400)
n2.next=n3
n4=Node(500)
n3.next=n4
print("before deleting 100")
obj.display()
print(" ")
print("after deleting 100")
obj.delete()
obj.display()
