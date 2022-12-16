#User function Template for python3
import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.minVal = data

class stack:
    def __init__(self):
        self.arr = []

    def push(self,x):
        if self.empty():
            self.arr.append(Node(x))
            return

        node = Node(x)
        currMin = self.getMin()

        if node.minVal < currMin:
            currMin = node.minVal
        else:
            node.minVal = currMin
        
        self.arr.append(node)

    def pop(self):
        if self.empty():
            return -1
        
        return self.arr.pop().data
        
    def empty(self) -> bool:
        return len(self.arr) == 0

    def getMin(self):
        if self.empty():
            return -1
            
        return self.arr[-1].minVal


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends