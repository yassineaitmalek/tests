class stack:

    def __init__(self):

        self.top=-1
        self.m=[]   

    def push(self,element):

        self.top+=1
        self.m+=[element]

    def pop(self) :

        if self.top < 0 :
            return("there is nothin to pop ")
        else :
            self.top-=1

    def get_top(self) :

        print(self.m[self.top])

    def print(self):

        print ("{",end=" ")
        for i in range(self.top,-1,-1) :
            print(self.m[i],end=" ")
        print("}")





s=stack()

s.push(1)
s.push(2)
s.push(3)
s.print()
s.get_top()
s.pop()
s.print()

















































