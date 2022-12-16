class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    
    def __init__(self):
        self.top = None
    
    def push(self, data):
        if self.top == None:
            self.top = StackNode(data)
            return
        
        newNode = StackNode(data)
        newNode.next = self.top
        self.top = newNode
        

    def pop(self):
        if self.top == None:
            return -1
        
        x = self.top
        val = x.data
        self.top = self.top.next
        del x
        
        return val
        
        
        



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends