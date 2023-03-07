class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head = None
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
        
    def display(self):
        if self.head is None:
            print("dll is empty")
        else:
            temp=self.head
        while(temp):
            print(temp.data,"<==>",end=" ")
            temp=temp.next
                    

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
obj.insert_pos(2)
obj.display()
