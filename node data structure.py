class node :
    def __init__(self,data=None):
        self.data=data
        self.next=None


class linkedlist :

    def __init__(self):
        self.root=node()

    def append(self,data):
        n=node(data)
        cur=self.root
        while cur.next!=None:
            cur=cur.next
        cur=n

    def lenght(self):
        cur=self.root
        size=0
        while cur.next!=None :
            size+=1
            cur=cur.next
        return size

    def display(self):
        cur=self.root
        while cur.next!=None:
            cur=cur.next
            print(cur.data)
            

    def get(self,index):
        if index > self.lenght() :
            print("Error")
            return None
        else :  
            cur_index=0
            cur=self.root
            a = True
            while a :
                cur=cur.next
                if cur_index==index :
                    a=False
                cur_index+=1
            return cur.data    


    def remove(self,index) :
        if index > self.lenght() :
            print("Error")
            return None
        else :
            cur_index=0
            cur=self.root
            a = True
            while a :
                lastnode=cur
                cur=cur.next
                if cur_index==index :
                    lastnode.next=cur.next
                cur_index+=1





l=linkedlist()

l.append(1)
l.append(2)
l.append(3)
l.display()
l.remove(1)
l.lenght()