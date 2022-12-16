# A linked list (LL) node 
# to store a queue entry 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
        
class MyQueue:
    
    def __init__(self):
        self.front = self.rear = None
    
    def push(self, item): 
        if self.front == None:
            self.front = self.rear = Node(item)
            return
        
        newNode = Node(item)
        self.rear.next = newNode
        self.rear = self.rear.next
        
    def pop(self):
        if self.front == None:
            return -1
        
        x = self.front
        val = x.data
        self.front = self.front.next
        del x
        
        return val
        


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends